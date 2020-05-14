from __future__ import absolute_import
from . import blocks, sb3_schema
import json
from jsonschema import Draft7Validator

class Parser():
    """A parser with which to parse Scratch projects.

    Typical usage example:

      from ccl_scratch_tools import Parser

      parser = Parser()

      blocks = parser.blockify("555555555.json")
    """

    def __init__(self):
        """Initializes parser."""

        self.block_data = blocks.blocks
        self.block_ignore = blocks.ignore
        self.event_listeners = blocks.event_listeners
        self.scratch_image_source = "https://assets.scratch.mit.edu/internalapi/asset/{0}/get/"
        self.sb3_schema = sb3_schema.sb3_schema

    def blockify(self, file_name=None, scratch_data=None):
        """Gets the statistics about a Scratch project.
        
        Args:
            file_name (str): the name of the Scratch JSON file to report on. (optional)
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON. (optional)

        Returns:
            A dictionary mapping function names (as in this class) to their results.

            If the data are invalid Scratch 3, returns False.
        
        Raises:
            ValueError: If neither file_name or scratch_data parameter is set.
        """

        if file_name is None and scratch_data is None:
            raise ValueError("Either file_name or scratch_data parameter is required.")

        try:
            if file_name is not None:
                with open(file_name) as f:
                    scratch_data = json.load(f)

            if scratch_data is not None and not self.is_scratch3(scratch_data):
                return False

            results = {
                "block_comments": self.get_block_comments(scratch_data),
                "blocks": self.get_blocks(scratch_data),
                "categories": self.get_categories(scratch_data),
                "comments": self.get_comments(scratch_data),
                "costumes": self.get_costumes(scratch_data),
                "sounds": self.get_sounds(scratch_data),
                "sprites": self.get_sprite_names(scratch_data),
                "variables": self.get_variables(scratch_data)
            }
            return results
        except:
            return False

    def get_block(self, block_id, scratch_data):
        """Returns the block object in the Scratch object given block ID.
        
        Args:
            block_id (str): the Scratch block ID in the project data structure.
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.

        Returns:
            A dictionary containing the block's information from the project data structure.
            Returns False if doesn't exist or if trouble accessing the data.
        """

        if self.is_scratch3(scratch_data):
            for target in scratch_data["targets"]:
                if block_id in target["blocks"]:
                    return target["blocks"][block_id]
            return False
        else:
            return False

    def get_block_comments(self, scratch_data):
        """Gets the comments left in a Scratch project, organized by block.
        
        Args:
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.

        Returns:
            A dictionary mapping blocks to a list of comments associated with them.
            If the input data is invalid, returns False.
        """

        try:
            comments = dict()
            for target in scratch_data["targets"]:
                if len(target["comments"]) > 0:
                    # Loop through blocks to see which comments go where
                    for block in target["blocks"]:
                        block = target["blocks"][block]
                        if "comment" in block and len(block["comment"]) > 0:
                            if block["opcode"] not in comments:
                                comments[block["opcode"]] = list()

                            comments[block["opcode"]].append(target["comments"][block["comment"]]["text"])
            return comments
        except:
            return False

    def get_block_name(self, opcode):
        """Gets the human-readable name of a Scratch block.
        
        Args:
            opcode (str): the Scratch opcode of the block.

        Returns:
            A string containing the block's human-readable name.

            If the opcode isn't listed in our block information, returns None.
        """

        for category in self.block_data:
            if opcode in self.block_data[category]:
                return self.block_data[category][opcode]

    def get_block_names(self, items, scratch_data=None):
        """Gets the human-readable name of a list of Scratch blocks.
        
        Args:
            items: a list of blocks to translate, whether a list of opcodes
                or a list of block IDs.
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.
                Include this only if items is a list of block IDs.

        Returns:
            A list containing the blocks' human-readable names.

            If the opcode isn't listed in our block information, that item of the list will be None.
        """

        names = list()
        if scratch_data is None:
            for item in items:
                names.append(self.get_block_name(item))
        else:
            for item in items:
                block = self.get_block(item, scratch_data)
                if block is False:
                    names.append(None)
                else:
                    names.append(self.get_block_name(block["opcode"]))

        return names

    def get_blocks(self, scratch_data):
        """Gets the blocks used in a Scratch project.
        
        Args:
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.

        Returns:
            A dictionary mapping used block opcodes to a list of block IDs
            (the IDs of the blocks of this type). Excludes unused blocks.

            If the input data is invalid, returns False.
        """

        try:
            blocks = dict()
            for target in scratch_data["targets"]:
                for block_id in target["blocks"]:
                    block = target["blocks"][block_id]
                    if block["opcode"] not in self.block_ignore:
                        if block["opcode"] not in blocks:
                            blocks[block["opcode"]] = list()
                        blocks[block["opcode"]].append(block_id)
            return blocks
        except:
            return False

    def get_categories(self, scratch_data):
        """Gets the categories of blocks used in a Scratch project.
        
        Args:
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.

        Returns:
            A dictionary mapping used block categories to the number of times they've been used.

            If the input data is invalid, returns False.
        """

        try:
            categories = dict.fromkeys(self.block_data, 0)
            for target in scratch_data["targets"]:
                for block in target["blocks"]:
                    block = target["blocks"][block]
                    for category in self.block_data:
                        if block["opcode"] in self.block_data[category]:
                            categories[category] += 1
            return categories
        except:
            return False

    def get_child_blocks(self, block_id, scratch_data):
        """Gets the child blocks of a given block.
        
        Args:
            block_id (str): The ID of the block whose children we're retrieving.
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.

        Returns:
            A list of block IDs, each of which corresponds to a child block of block_id.
            The first element of the list will be the block_id argument passed in.
            Returns False if data are invalid.
        """

        if self.is_scratch3(scratch_data):
            children = [block_id]
            for target in scratch_data["targets"]:
                if block_id in target["blocks"]:
                    # If this is a block that can have substacks, like loops or conditions
                    if "SUBSTACK" in target["blocks"][block_id]["inputs"]:
                        children += self.loop_through_blocks(target["blocks"][block_id]["inputs"]["SUBSTACK"][1], scratch_data)
                    # If this is a block that doesn't have substacks but functionally operates like it does
                    elif target["blocks"][block_id]["opcode"] in self.event_listeners:
                        children += self.loop_through_blocks(target["blocks"][block_id]["next"], scratch_data)
            return children
        return False

    def get_comments(self, scratch_data):
        """Gets the comments left in a Scratch project.
        
        Args:
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.

        Returns:
            A list of comments in the project.

            If the input data is invalid, returns False.
        """

        try:
            comments = list()
            for target in scratch_data["targets"]:
                for comment in target["comments"]:
                    comments.append(target["comments"][comment]["text"])
            return comments
        except:
            return False

    def get_costumes(self, scratch_data):
        """Gets the costumes used in a Scratch project.
        
        Args:
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.

        Returns:
            A list of the names of the costumes used.

            If the input data is invalid, returns False.
        """

        try:
            costumes = list()
            for target in scratch_data["targets"]:
                for costume in target["costumes"]:
                    costumes.append(costume["name"])
            return costumes
        except:
            return False

    def get_sounds(self, scratch_data):
        """Gets the sounds used in a Scratch project.
        
        Args:
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.

        Returns:
            A list of the names of the sounds used.

            If the input data is invalid, returns False.
        """

        try:
            sounds = list()
            for target in scratch_data["targets"]:
                for sound in target["sounds"]:
                    sounds.append(sound["name"])
            return sounds
        except:
            return False

    def get_sprite(self, block_id, scratch_data):
        """Gets the sprite with which a block is associated.
        
        Args:
            block_id (str): the Scratch block ID in the project data structure.
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.

        Returns:
            A dictionary containing the sprite's information from the project data structure,
            including sprite name, current costume asset ID, and current costume image URL.
            Returns False if doesn't exist or if trouble accessing the data.
        """

        result = self.get_target(block_id, scratch_data)
        if result == False:
            return False

        target, i = result
        sprite = {
            "index": i,
            "name": target["name"],
            "costume_asset": target["costumes"][target["currentCostume"]]["assetId"],
            "costume_asset_url": self.scratch_image_source
                .format(target["costumes"][target["currentCostume"]]["md5ext"])
        }
        return sprite

    def get_sprite_names(self, scratch_data):
        """Get a list of sprite names, not including the stage targets.
        
        Args:
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.
        Returns:
            A list of sprite names. Stage targets are excluded. False if unsuccessful.
        """
        if not self.is_scratch3(scratch_data):
            return False

        sprites = list()
        for target in scratch_data["targets"]:
            if not target["isStage"]:
                sprites.append(target["name"])
        return sprites

    def get_surrounding_blocks(self, block_id, scratch_data, count=5, delve=False):
        """Gets the surrounding blocks given a block ID.
        
        Args:
            block_id (str): The ID of the block of which to capture surrounding blocks.
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.
            count (int): The maximum number of blocks you want to capture, including block_id.
                Defaults to 5.
            delve (bool): Whether we should only return child blocks if this block has children,
                as with loops or event listeners.

        Returns:
            An ordered list of the IDs of the blocks surrounding block_id,
            including block_id in the middle. Returns False if the block_id doesn't exist,
            or if the data are invalid.
        """
        
        before = (count - 1) // 2
        after = count - 1 - before

        if self.is_scratch3(scratch_data):
            for target in scratch_data["targets"]:
                if block_id in target["blocks"]:
                    children = self.get_child_blocks(block_id, scratch_data)

                    # If we just want children and we have children
                    if delve and len(children) > 1:
                        return children[0:count]
                    # If we don't want just children but we do have children
                    elif not delve and len(children) > 1:
                        before_blocks = self.loop_through_blocks(block_id, scratch_data, mode="parent")
                        before_blocks = before_blocks[1:before + 1]
                        before_blocks.reverse()

                        return before_blocks + children[0:after + 1]
                    # If we don't have children
                    else:
                        before_blocks = self.loop_through_blocks(block_id, scratch_data, mode="parent")
                        after_blocks = self.loop_through_blocks(block_id, scratch_data, mode="next")
                        before_blocks = before_blocks[1:before + 1]
                        before_blocks.reverse()

                        return before_blocks + after_blocks[0:after + 1]
        return False
        
    def get_target(self, block_id, scratch_data):
        """Returns the target a block is part of.
        
        Args:
            block_id (str): find the target this block is part of.
            scratch_data (dict): the Scratch project to search through.

        Returns:
            A tuple. First, a dictionary representing the relevant target;
            second, the index of this target in the project's target list.
            
            Returns False if unsuccessful.
        """
        if not self.is_scratch3(scratch_data):
            return False
        
        for i in range(len(scratch_data["targets"])):
            target = scratch_data["targets"][i]
            if block_id in target["blocks"]:
                return target, i
                
        return False

    def get_variables(self, scratch_data):
        """Gets the variables used in a Scratch project.
        
        Args:
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.

        Returns:
            A list of the names of the variables used.

            If the input data is invalid, returns False.
        """

        try:
            variables = list()
            for target in scratch_data["targets"]:
                for variable in target["variables"]:
                    variables.append(target["variables"][variable][0])
            return variables
        except:
            return False

    def is_scratch3(self, scratch_data):
        """Checks a supposed Scratch data file against the Scratch 3 schema.
        
        Args:
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.

        Returns:
            True if the data matches the Scratch 3 schema. Otherwise False.
        """

        return Draft7Validator(self.sb3_schema).is_valid(scratch_data)

    def loop_through_blocks(self, block_id, scratch_data, mode="next"):
        """Loops through blocks in forward or backward direction.
        
        Args:
            block_id (str): The ID of the block where we start our loop.
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.
            mode (str): The mode in which we're looping -- "next" or "parent". Defaults to "next".

        Return:
            A list of block IDs, each of which corresponds to a block related to block_id.
            The first element of the list will be the block_id argument passed in.
            Returns False if data or arguments are invalid.
        """

        if mode not in ["next", "parent"]:
            return False

        if self.is_scratch3(scratch_data):
            blocks = [block_id]
            for target in scratch_data["targets"]:
                if block_id in target["blocks"]:
                    next_block = target["blocks"][block_id][mode]
                    while next_block is not None:
                        blocks.append(next_block)
                        next_block = target["blocks"][next_block][mode]
            return blocks
            
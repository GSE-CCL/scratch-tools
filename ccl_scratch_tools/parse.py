import ccl_scratch_tools.blocks
import json

class Parser():
    """A parser with which to parse Scratch projects.

    Typical usage example:

      from ccl_scratch_tools import Parser

      parser = Parser()

      blocks = parser.blockify("555555555.json")
    """

    def __init__(self):
        """Initializes parser with studio and project URLs."""

        self.block_data = blocks.blocks
        self.block_ignore = blocks.ignore

    def blockify(self, file_name):
        """Gets the statistics about a Scratch project.
        
        Args:
            file_name (str): the name of the Scratch JSON file to report on.

        Returns:
            A dictionary mapping function names (as in this class) to their results.

            If the file couldn't be opened, returns False.
        """

        try:
            with open(file_name) as f:
                scratch_data = json.load(f)
            results = {
                "block_comments": self.get_block_comments(scratch_data),
                "blocks": self.get_blocks(scratch_data),
                "categories": self.get_categories(scratch_data),
                "comments": self.get_comments(scratch_data),
                "costumes": self.get_costumes(scratch_data),
                "sounds": self.get_sounds(scratch_data),
                "variables": self.get_variables(scratch_data)
            }
            return results
        except:
            return False

    def get_blocks(self, scratch_data):
        """Gets the blocks used in a Scratch project.
        
        Args:
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.

        Returns:
            A dictionary mapping used block names to the number of times they've been used. Excludes unused blocks.

            If the input data is invalid, returns False.
        """

        try:
            blocks = dict()
            for target in scratch_data["targets"]:
                for block in target["blocks"]:
                    block = target["blocks"][block]
                    if block["opcode"] not in self.block_ignore:
                        if block["opcode"] not in blocks:
                            blocks[block["opcode"]] = 0
                        blocks[block["opcode"]] += 1
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
    
    def get_block_comments(self, scratch_data):
        """Gets the comments left in a Scratch project, organized by block.
        
        Args:
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.

        Returns:
            comments: a dictionary mapping blocks to a list of comments associated with them.

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

    def get_comments(self, scratch_data):
        """Gets the comments left in a Scratch project.
        
        Args:
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.

        Returns:
            comments: a list of comments in the project.

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
            costumes: a list of the names of the costumes used.

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
            costumes: a list of the names of the sounds used.

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

    def get_variables(self, scratch_data):
        """Gets the variables used in a Scratch project.
        
        Args:
            scratch_data (dict): a Python dictionary representing the imported Scratch JSON.

        Returns:
            costumes: a list of the names of the variables used.

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

from __future__ import absolute_import
from ccl_scratch_tools.scratch_to_blocks import blocks

class Visualizer():
    """A way to visualize blocks by exporting to Scratchblocks syntax.

    Typical usage example:

      from ccl_scratch_tools import Visualizer

      visualizer = Visualizer()

      scratchblocks = visualizer.generate_scratchblocks(scratch_data)
    """

    def __init__(self):
        """Initializes visualizer."""
        return

    def generate_scratchblocks(self, scratch_data):
        """Generates all blocks in a project.
    
        Args:
            scratch_data (dict): the Scratch project to process.
        Returns:
            A list of scripts in the project that can be turned into text. False if unsuccessful.
        """

        if "targets" not in scratch_data:
            return False

        return blocks.generate_scratchblocks(scratch_data)

    def generate_script(self, block_id, block_list, block_ids=None, text=False):
        """Generates a script dictionary, nesting the blocks as appropriate.
        
        Args:
            block_id (str): generate the script starting from this block.
            block_list (array-like): the full list of blocks within this target.
            block_ids (array-like) (optional): the set of block IDs that are allowed to be added.
                If not provided, then all blocks are allowed.
            text (boolean) (optonal): whether to return this in Scratchblocks text syntax.
                If not provided, defaults to False - it'll just return the script dictionary.
        
        Returns:
            A dictionary with the nesting of this script as appropriate. False if unsuccessful.
        """

        script = blocks.generate_script(block_id, block_list, block_ids=None)
        if script is None or script == False:
            return False
        
        if text:
            return blocks.block_string([script])
        else:
            return script

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
        if "targets" not in scratch_data:
            return False
        
        for i in range(len(scratch_data["targets"])):
            target = scratch_data["targets"][i]
            if block_id in target["blocks"]:
                return target, i
                
        return False

import numpy as np


class Joint:
    def __init__(self, name, parent=None, children=None):
        self.name = name
        self.parent = parent
        self.children = children


class MocapData:
    def __init__(self):
        self.skeleton = {}
        self.values = None
        self.channel_names = []
        self.framerate = 0.0
        self.root_name = ""

    def traverse(self, j=None):
        stack = [self.root_name]
        while stack:
            joint = stack.pop()
            yield joint
            for c in self.skeleton[joint]["children"]:
                stack.append(c)

    def clone(self):
        import copy

        new_data = MocapData()
        new_data.skeleton = copy.copy(self.skeleton)
        new_data.values = copy.copy(self.values)
        new_data.channel_names = copy.copy(self.channel_names)
        new_data.root_name = copy.copy(self.root_name)
        new_data.framerate = copy.copy(self.framerate)
        return new_data

    def get_all_channels(self):
        """Returns all of the channels parsed from the file as a 2D numpy array"""

        frames = [f[1] for f in self.values]
        return np.asarray([[channel[2] for channel in frame] for frame in frames])

    def get_skeleton_tree(self):
        skeleton_tree = []
        for joint_name, joint_data in self.skeleton.items():
            for child in joint_data["children"]:
                skeleton_tree.append([joint_name, child])
        return skeleton_tree

import os
import random

class GeneratePairs:
    """
    Generate the pairs.txt file that is used for training face classifier when calling python `src/train_softmax.py`.
    Or others' python scripts that needs the file of pairs.txt.
    Doc Reference: http://vis-www.cs.umass.edu/lfw/README.txt
    """

    def __init__(self, data_dir, pairs_filepath, img_ext):
        """
        Parameter data_dir, is your data directory.
        Parameter pairs_filepath, where is the pairs.txt that belongs to.
        Parameter img_ext, is the image data extension for all of your image data.
        """
        self.data_dir = data_dir
        self.pairs_filepath = pairs_filepath
        self.img_ext = img_ext


    def generate(self):
        self._generate_matches_pairs()
        self._generate_mismatches_pairs()


    def _generate_matches_pairs(self):
        """
        Generate all matches pairs
        """
        folders = os.listdir(self.data_dir)
        random.shuffle(folders)
        for name in folders:
            a = []

            for file in os.listdir(self.data_dir + name):
                a.append(file)

            with open(self.pairs_filepath, "a") as f:
                for i in range(3):
                    temp = random.choice(a).split("_") # This line may vary depending on how your images are named.
                    w = '_'.join(temp[:-1])
                    l = random.choice(a).split("_")[-1].lstrip("0").rstrip(self.img_ext)
                    r = random.choice(a).split("_")[-1].lstrip("0").rstrip(self.img_ext)
                    f.write(w + "\t" + l + "\t" + r + "\n")


    def _generate_mismatches_pairs(self):
        """
        Generate all mismatches pairs
        """
        folders = os.listdir(self.data_dir)
        random.shuffle(folders)
        for i, name in enumerate(folders):
            remaining = os.listdir(self.data_dir)
            del remaining[i] # deletes the file from the list, so that it is not chosen again

            with open(self.pairs_filepath, "a") as f:
                for i in range(3):
                    other_dir = random.choice(remaining)
                    file1 = random.choice(os.listdir(self.data_dir + name))
                    file2 = random.choice(os.listdir(self.data_dir + other_dir))
                    f.write(name + "\t" + file1.split("_")[-1].lstrip("0").rstrip(self.img_ext) + "\t"
                      + other_dir + "\t" + file2.split("_")[-1].lstrip("0").rstrip(self.img_ext) + "\n"
                    )


if __name__ == '__main__':
    data_dir = "/content/drive/MyDrive/Github/datasets/korean-face/validate/"
    pairs_filepath = "/content/drive/MyDrive/Github/datasets/korean-face/pairs.txt"
    img_ext = ".jpg"
    generatePairs = GeneratePairs(data_dir, pairs_filepath, img_ext)
    generatePairs.generate()
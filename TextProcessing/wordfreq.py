import clearwords


class CountWordFrequency(object):
    """
    This class will be processing the file and removes the punctuations
    If you want to remove the noise words also from the file then pass the
    is_noise_words parameter while initializing the class

    Noise Word list is taken from here
    https://gist.github.com/sebleier/554280

    All punctuations list is taken from the string module string.punctuation
    """
    def __init__(self, file_name, is_noise_words=False):
        self.file_name = file_name
        self.noise_words_list = self.check_noise_words(is_noise_words)

    def check_noise_words(self, is_noise_words):
        """
        check for the noise words if user wants to remove the noise words from the file
        Args:
            is_noise_words (boolean): by default False
        returns:
            List of noise words
        Raise:
            Exception if the provided noise wards list file is not available
        """
        if is_noise_words:
            try:
                nf = open("stop_words_list.txt", "r")
            except IOError as ex:
                raise "No such file or directory found, please try with valid file"

            return nf.read().lower().replace("\n", " ")

        return []

    def read_file_text(self):
        """
        Method to read the provided file data
        return:
            file text data by removing new line char
        """
        try:
            f = open(self.file_name, 'r')
        except IOError as ex:
            raise "No such file or director found, please try with valid file"

        # read the file data
        file_text = f.read()
        # remove the new line chars
        file_text = file_text.replace("\n", " ")
        return file_text

    def count_occurrences(self):
        """
        :return:
        """
        file_text = self.read_file_text()
        if file_text:
            # call the util to remove the punctuations
            data = clearwords.clear_words(file_text)
            if self.noise_words_list:
                # remove the noise words from the list if file is having noise words
                data = [word for word in data if word not in self.noise_words_list]
            data_with_count = [{item: data.count(item)} for item in set(data)]
            return data_with_count

        return


c = CountWordFrequency('noise_words.txt', is_noise_words=True)
print c.count_occurrences()

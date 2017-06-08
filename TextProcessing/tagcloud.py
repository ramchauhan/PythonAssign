from wordfreq import CountWordFrequency


class GenerateCloudTag(CountWordFrequency):
    """
    Generate the html tag Could
    """
    def process_words_for_tag(self):

        words = self.count_occurrences()
        sorted_words = sorted(words, key=lambda x: (x.keys(), x.values()))
        return sorted_words

    def write_cloud_tag(self, output_file):
        sorted_words = self.process_words_for_tag()
        output_f = open(output_file, 'w')
        output_f.write("<style type=\"text/css\">\n")
        output_f.write(".smallest {font-size: 10px;}\n")
        output_f.write(".small {font-size: 15px;}\n")
        output_f.write(".medium {font-size: 20px;}\n")
        output_f.write(".large {font-size: 25px;}\n")
        output_f.write(".extra_large {font-size: 32px;}\n")
        output_f.write(".largest {font-size: 40px;}\n")
        output_f.write("</style>\n")
        css_style_map = ["smallest", "small", "medium", "large", "extra_large", "largest"]

        for tag in sorted_words:
            if tag.values()[0] > 5:
                output_f.write("<span class=\"" + css_style_map[5] + "\">" + tag.keys()[0] + "</span> ")
            else:
                output_f.write("<span class=\"" + css_style_map[tag.values()[0]] + "\">" + tag.keys()[0] + "</span> ")
        output_f.close()


# Test for the working
gt = GenerateCloudTag('noise_words.txt', is_noise_words=True)
opt = gt.write_cloud_tag("out.html")


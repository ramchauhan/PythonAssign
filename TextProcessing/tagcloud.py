from wordfreq import CountWordFrequency


class GenerateCloudTag(CountWordFrequency):
    """
    Generate the html tag Could
    """
    def process_words_for_tag(self):
        words = self.count_occurrences()
        sorted_words = sorted(words, key=lambda x: (x.values(), x.keys()))
        return sorted_words

    def write_cloud_tag(self, output_file):
        sorted_words = self.process_words_for_tag()
        output_f = open(outputfile, 'w')
        outputf.write("<style type=\"text/css\">\n")
        outputf.write(".smallest {font-size: 10px;}\n")
        outputf.write(".small {font-size: 15px;}\n")
        outputf.write(".medium {font-size: 20px;}\n")
        outputf.write(".large {font-size: 25px;}\n")
        outputf.write(".extra_large {font-size: 32px;}\n")
        outputf.write(".largest {font-size: 40px;}\n")
        outputf.write("</style>\n")
        css_style_map = ["smallest", "small", "medium", "large", "extra_large", "largest"]

        for tag in sorted_words:
            if tag.values()[0] > 5:
                output_f.write("<span class=\"" + css_style_map[5] + "\">" + tag.keys()[0] + "</span> ")
            else:
                output_f.write("<span class=\"" + css_style_map[tag.values()[0]] + "\">" + tag.keys()[0] + "</span> ")
        outputf.close()

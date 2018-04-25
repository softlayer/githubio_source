---
title: "buildExamples.py"
description: "buildExamples.py"
date: "2018-04-25"
classes: 
tags:
    - "."
---


```
import os 
from pprint import pprint as pp
import re
import time

template = """---
title: "{title}"
description: "{description}"
date: "{date}"
classes: {classes}
tags:
{tags}
---


```
{example}
```
"""

class examples():

    def main(self):
        out_dir = '/Users/christopher/Code/githubio_source/content'
        for root, dirs, files in os.walk("."):
            path = root.split(os.sep)
            # pp(path)
            # print((len(path) - 1) * '---', os.path.basename(root))
            for file in files:
                # print(len(path) * '---', file)
                print("Working on %s" % file)
                output = self.buildExample(file, root)
                out_folder = self.exampleType(file)
                if out_folder:
                    out_file = open("%s/%s/%s.md" % (out_dir, out_folder, file), "w")
                    out_file.write(output)
                    out_file.close()


    def buildExample(self, file, path):
        fullPath = "%s/%s" % (path, file)
        print("\t%s" % fullPath)
        with open(fullPath, 'r') as myfile:
            data = myfile.read()
        sl_regex = re.compile(r"(SoftLayer_([A-Z]{1}[a-z]+[_]?)+)", re.MULTILINE)
        sl_classes = sl_regex.findall(data)
        class_list = []
        for i in sl_classes:
            class_list.append(i[0])
        class_list = set(class_list)
        class_string = ""
        for i in class_list:
            class_string = '%s\n    - "%s"' % (class_string, i)

        print(class_string)
        tags = path.split(os.sep)[-1]
        tags = '    - "%s"' % tags.replace(r" ", "").lower()
        print("Tags: %s "  % tags) 
        modify_date = time.strftime("%Y-%m-%d", time.localtime(os.path.getmtime(fullPath)))
        
        print("Date: %s" % modify_date)
        out_string = template.format(title=file, description=file, date=modify_date, classes=class_string, tags=tags, 
            example=data)
        return out_string
    
    def exampleType(self, file):
        type_map = {'go':'go', 'txt': 'rest', 'py': 'python', 'php': 'php',
                     'java': 'java', 'cs': 'csharp', 'rb': 'ruby', 'pl': 'perl', 'json': 'rest'}
        extension = file.split('.')[-1]
        if extension in type_map:
            return type_map[extension]
        return False

if __name__ == "__main__":
    main = examples()
    main.main()
```

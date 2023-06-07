import fnmatch
import re
import os
import mkdocs
import mkdocs.plugins
import mkdocs.structure.files
from . import logger as log

class IncludeFolders(mkdocs.plugins.BasePlugin):
    """A mkdocs plugin that adds all matching files from the input list."""

    config_scheme = (
        ('ext', mkdocs.config.config_options.Type((str, list), default=[
            ".md", ".markdown", ".mdown", ".mkdn", ".mkd", ".css",
            ".js", ".javascript", ".html", ".htm", ".xml", ".json",
            ".bmp", ".tif", ".tiff", ".gif", ".svg", ".jpeg",
            ".jpg", ".jif", ".jfif", ".jp2", ".jpx", ".j2k",
            ".j2c", ".fpx", ".pcd", ".png", ".pdf", "CNAME",
            ".snippet", ".pages"
        ])),
        ('glob', mkdocs.config.config_options.Type((str, list), default=None)),
        ('regex', mkdocs.config.config_options.Type((str, list), default=None)),
        ('priority_path', mkdocs.config.config_options.Type((str, list), default=None))
    )

    def on_files(self, files, config):
        exts = self.config['ext'] or []
        if not isinstance(exts, list):
            exts = [exts]
        globs = self.config['glob'] or []
        if not isinstance(globs, list):
            globs = [globs]
        regexes = self.config['regex'] or []
        if not isinstance(regexes, list):
            regexes = [regexes]
        paths = self.config['priority_path'] or []
        if not isinstance(paths, list):
            paths= [paths]
        out = []
        docfiles = {}
        filesplit = []
        
        #log.info(f"self {self}\n\nconfig {config}\n\nfiles {files}\n\nexts {exts}\n\nglobs {globs}\n\nregex {regexes}")
        #print(f"{config['docs_dir']}")
        for f in files:
            split = re.split("/",f.src_uri)
            if not split[0] in filesplit:
                filesplit.append(split[0])
                print(f" folder {split}")
            if fnmatch.fnmatchcase(f.src_uri,"assets/*"):
                print(f"    asset {split}")
            print(f" - file {f.name}, doc {f.is_documentation_page}, stat {f.is_static_page}, media {f.is_media_file}, js {f.is_javascript}, css {f.is_css}")

        def prioritize_files(path):
            print(f"\n!! Prioritize {path}")
            i=0
            for f in files:
                #if i<10:
                #print(f"- check {path} in {f.src_uri},  {fnmatch.fnmatchcase(f.src_uri,path)}")
                if fnmatch.fnmatchcase(f.src_uri,path):
                    index = re.sub(path,"",f.url)#.replace(path+"/","")
                    #print(f" index: {index}")
                    if index in docfiles:
                        print(f"- already found {index}, src {docfiles[index]}")
                        continue
                    f.src_uri = re.sub(path,"",f.src_uri)
                    #f.abs_src_path = re.sub(path,"",f.abs_src_path)
                    f.abs_dest_path = re.sub(path,"",f.abs_dest_path)
                    f.dest_uri = re.sub(path,"",f.dest_uri)
                    f.url = index #f.url.replace(path+"/","")
                    docfiles[index] = f #{'src':f.src_uri,'abs':f.abs_dest_path,'url':f.url}
                    #if i<10:
                    #    print(f"- pri {index}, docfiles {docfiles[index]}, abs {f.abs_dest_path}")
                    i=i+1
                if fnmatch.fnmatchcase(f.src_uri,"assets/*"):
                    docfiles[f.src_uri] = f
                    print(f"- adding assets {f.src_uri}")

        for p in paths:
            prioritize_files(p)
        

        #print(f"\n\nDoc files: \n {docfiles}")
        print("\n\nStart outputing files\n")
        for key in docfiles:
            file = docfiles[key]
            out.append(file)
        #print(f"\n Out files: {out} ")
        return mkdocs.structure.files.Files(out)

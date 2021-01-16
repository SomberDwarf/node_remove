# node_remove

This python script is for editing the compressed sub files used in Barotrauma.  node_remove scans the compressed xml file for wire nodes and removes all intermediate nodes, leaving only the the origin and termination coordinates.

## Description

Sometimes wiring in the subeditor gets to be such a mess that it's easier to startover.  Also useful if you need a clean copy for mirroring.  This is a python based script that decompresses the sub file, edits the xml and recompresses the file.

## Getting Started

Run the script or binary.  Select file, a backup is created and the sub file is replaced with the changed version.

### Dependencies

* python 3.x
* or windows binary

### Installing / Executing

* run script or executable
```
python node_remove.py
```
* navigate it to the folder containing your_submarine.sub
* accept
* If it's not already in the submaring directory, place resulting .sub file in your barotrauma submarines folder

## Windows binary

* [node_remove.exe](https://github.com/SomberDwarf/node_remove/releases/download/v1.0.1/node_remove.exe)

## Help

Always make your own backups.

## Authors
SomberDwarf
You can find me on the barotrauma discord
[@SomberDwarf](https://discord.com/invite/undertow)

## Version History

* 1.0.1
    * Initial Release

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [gzip](https://github.com/matiassingers/awesome-readme)
* [xml.etree.elementtree](https://docs.python.org/3/library/xml.etree.elementtree.html)
* [Pyinstaller](https://github.com/pyinstaller/pyinstaller)
* [Barotrauma](https://barotraumagame.com/)
* [Barotrauma github](https://github.com/Regalis11/Barotrauma)

# ColorFrame: Add Colored Borders to Your Pictures

A simple script to created add a colored frame onto my photography pictures.

## Install

This code is compatible with `Python 3.6+`.
Install it in your virtual enrivonment with:
```bash
pip install colorframe
```

## Usage

With this package is installed in the activated enrivonment, usage is:
```bash
python -m colorframe -p path_to_files
```

Detailed options go as follows:
```bash
usage: __main__.py [-h] -p PATH [-hv VERTICAL_BORDER] [-hb HORIZONTAL_BORDER]
                   [-c COLOR] [-l LOG_LEVEL]

Adding a color frame border to your images.

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Path to the file or directory of file to add a
                        whiteframe to.
  -hv VERTICAL_BORDER, --vertical_border VERTICAL_BORDER
                        Size (width) of the whiteframe to add on the vertical
                        image edges. Defaults to 150.
  -hb HORIZONTAL_BORDER, --horizontal_border HORIZONTAL_BORDER
                        Size (height) of the whiteframe to add on the
                        horizontal image edges. Defaults to 150.
  -c COLOR, --color COLOR
                        The desired color of the added border. Should be a
                        keyword recognized by Pillow. Defaults to 'white'.
  -l LOG_LEVEL, --logs LOG_LEVEL
                        The logging level. Defaults to 'info'.
```

The script will crawl files, add borders and export the results in a newly created `outputs` folder.

## License

Copyright &copy; 2020 Felix Soubelet. [MIT License](LICENSE)

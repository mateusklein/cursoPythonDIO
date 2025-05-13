# package_name

Description. 
The package package_name is used to:
	Processing
		- Histogram matching 
		- Structural similiarity
		- Resize image
	Utils:
		- Read image
		- Save image
		- Plot image
		- Plot result
		- Plot histograms

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package_name

```bash
python -m pip install --upgrade pip
python -m pip install --user twine
python -m pip install --user setuptools
python setup.py sdist bdist_whell
pip install package_name
```

## Usage

```python
from image_processing.processing import combination
from image_processing.processing import transformation
from image_processing.utils import io
from image_processing.utils import plot
combination.find_difference()
combination.transfer_histogram()
transformation.resize_image()
io.read_image()
io.save_image()
plot.plot_image()
plot.plot_result()
plot.plot_histogram()
```

## Author
Mateus

## License
[MIT](https://choosealicense.com/licenses/mit/)
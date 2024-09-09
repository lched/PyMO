# PyMO
A library for using motion capture data for machine learning

**This library is currently highly experimental and everything is subject to change :)**


## Roadmap
* Mocap Data Parsers and Writers
* Common mocap pre-processing algorithms
* Feature extraction library
* Visualization tools

## Current Features
* [Read BVH Files](#read-bvh-files)
* Write BVH Files
* Pre-processing pipelines
    * [Supporting `scikit-learn` API](#scikit-learn-pipeline-api)
    * Convert data representations
        * [Euler angles to positions](#convert-to-positions)
        * Euler angles to exponential maps
        * Exponential maps to euler angles
    * Body-oriented global translation and rotation calculation with inverse tranform
    * Root-centric position normalizer with inverse tranform
    * Standard scaler
    * Joint selectors
* Annotations
    * Foot/ground contact detector


### Read BVH Files

```python
from pymo.parsers import BVHParser

parser = BVHParser()

parsed_data = parser.parse('demos/data/AV_8Walk_Meredith_HVHA_Rep1.bvh')
```


### scikit-learn Pipeline API

```python

from pymo.preprocessing import *
from sklearn.pipeline import Pipeline

data_pipe = Pipeline([
    ('param', MocapParameterizer('position')),
    ('rcpn', RootCentricPositionNormalizer()),
    ('delta', RootTransformer('abdolute_translation_deltas')),
    ('const', ConstantsRemover()),
    ('np', Numpyfier()),
    ('down', DownSampler(2)),
    ('stdscale', ListStandardScaler())
])

piped_data = data_pipe.fit_transform([parsed_data])
```

### Convert to Positions

```python
mp = MocapParameterizer('position')

positions = mp.fit_transform([parsed_data])
```


### Foot/Ground Contact Detector
```python
from pymo.features import *

plot_foot_up_down(positions[0], 'RightFoot_Yposition')
```

![Foot Contact](assets/foot_updown.png)

```python
signal = create_foot_contact_signal(positions[0], 'RightFoot_Yposition')
plt.figure(figsize=(12,5))
plt.plot(signal, 'r')
plt.plot(positions[0].values['RightFoot_Yposition'].values, 'g')
```

![Foot Contact Signal](assets/footcontact_signal.png)

## Feedback, Bugs, and Questions
For any questions, feedback, and bug reports, please use the [Github Issues](https://github.com/omimo/PyMO/issues).

## Credits
Created by [Omid Alemi](https://omid.al/projects/)


## License
This code is available under the [MIT license](http://opensource.org/licenses/MIT).

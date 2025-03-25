from trdg.generators import (
    GeneratorFromDict,
    GeneratorFromRandom,
    GeneratorFromStrings,
    GeneratorFromWikipedia,
)

# The generators use the same arguments as the CLI, only as parameters
generator = GeneratorFromStrings(
    ['Ra25', 'φ2.3', '127±3', 'M24×1.5-7H'],
    # blur=2,
    # random_blur=True,
    size=20,
    language='cn',
    count=10,
    # margins=(1, 1, 1, 1),
)

idx = 0
for img, lbl in generator:
    print(idx, img, lbl)
    img.save(f'./out/{idx}.jpg')
    idx = idx + 1
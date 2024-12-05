# moondream-0.5b Cog Model

This is an implementation of [vikhyatk/moondream0.5b](https://huggingface.co/vikhyatk/moondream2) as a [Cog](https://github.com/replicate/cog) model.

## Development

Follow the [model pushing guide](https://replicate.com/docs/guides/push-a-model) to push your own model to [Replicate](https://replicate.com).


## How to use

Make sure you have [cog](https://github.com/replicate/cog) installed.

To run a prediction:

    cog predict -i image=@demo-1.jpg -i prompt="What color is the girl's hair?"

## Output

    The girl's hair is gray.
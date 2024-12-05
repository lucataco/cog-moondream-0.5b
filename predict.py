# Prediction interface for Cog ⚙️
# https://cog.run/python

from cog import BasePredictor, Input, Path
from PIL import Image
import moondream as md

CHECKPOINT_PATH = "checkpoints/moondream-0_5b-int8.mf"

class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load the model into memory to make running multiple predictions efficient"""
        self.model = md.vl(model=CHECKPOINT_PATH)

    def predict(
        self,
        image: Path = Input(description="Input image"),
        prompt: str = Input(
            description="Question to ask about the image",
            default="Describe this image"
        ),
    ) -> str:
        """Run a single prediction on the model"""
        # Load and process image
        img = Image.open(image)
        encoded_image = self.model.encode_image(img)
        
        # Generate response based on prompt
        if prompt.lower().strip() == "describe this image":
            result = self.model.caption(encoded_image)
            return result["caption"]
        else:
            result = self.model.query(encoded_image, prompt)
            return result["answer"]

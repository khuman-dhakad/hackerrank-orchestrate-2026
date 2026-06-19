import os
import json
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")
USE_GEMINI = True


def analyze_image(image_path, claim_text, claim_object):
    image = Image.open(image_path)

    prompt = f"""
You are an insurance damage reviewer.

Claim Object: {claim_object}

Claim:
{claim_text}

Your task is to verify the user's specific claim.

Focus on the claimed damage and claimed object part.

Do not report unrelated damage if it is not relevant to the claim.

If the claimed damage is visible anywhere in the image, return supported.

A small scratch, minor dent, or light cosmetic damage still counts as supported.

Do not require severe damage.

If the claimed area is visible and no such damage exists, return contradicted.

If the claimed area is not visible, return not_enough_information.

Analyze the image and return ONLY valid JSON.

Required JSON format:
  Allowed issue_type values:
dent
scratch
crack
glass_shatter
broken_part
missing_part
torn_packaging
crushed_packaging
water_damage
stain
none
unknown

Allowed severity values:
none
low
medium
high
unknown

Allowed car object_part values:
front_bumper
rear_bumper
door
hood
windshield
side_mirror
headlight
taillight
fender
quarter_panel
body
unknown

Allowed laptop object_part values:
screen
keyboard
trackpad
hinge
lid
corner
port
base
body
unknown

Allowed package object_part values:
box
package_corner
package_side
seal
label
contents
item
unknown

Return values EXACTLY as written above.
{{
  "issue_type": "",
  "object_part": "",
  "claim_status": "",
  "severity": "",
  "reason": ""
}}

claim_status rules:

supported:
The claimed damage exists and is visible.

contradicted:
The claimed area is visible and the claimed damage is definitely not present.

not_enough_information:
The claimed area cannot be inspected from the provided image.

Return ONLY one of:
supported
contradicted
not_enough_information
"""

    try:
        if USE_GEMINI:
            response = model.generate_content(
                [prompt, image]
            )
            return response.text
    except Exception as e:
        print("Gemini Error:", e)
        print("Using fallback mode...")

    fallback = {
        "issue_type": "unknown",
        "object_part": "unknown",
        "claim_status": "not_enough_information",
        "severity": "unknown",
        "reason": "Fallback mode used because Gemini was unavailable."
    }

    return json.dumps(fallback)

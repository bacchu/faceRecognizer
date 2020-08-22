import json
import numpy
from json import JSONEncoder

#This is the file where the 128D data is being generated. We created the file below:
import facevector_generator

#This class serializes a NumPy array into a JSON format output
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


# Replace the string below with the full file path and image in your local directory
photoFile = 'images/claire_dearing_image1.jpg'

# Call the function 'generate_vector' that resides in facevector_generator.py
# Get the 128D encodings back from that function
encodings_128D = facevector_generator.generate_vector(photoFile)

#Create a dictionary object to store the output data
face_vector_dict = {
    'faceVector': encodings_128D,
    'result': 'Success',
    'message': '',
    'errorCode': 0
}

#Create a JSON object with the output data
json_encodings = json.dumps(face_vector_dict, cls=NumpyArrayEncoder, indent=2)
print(json_encodings)

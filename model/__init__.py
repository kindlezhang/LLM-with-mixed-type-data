
import sys
sys.path.append(r"/Users/kindle/Desktop/file/project/LLM-with-mixed-type-data")
from model.cnn import simplecnn
from model.resnet import resnet18, resnet50
from model.vit import vit_base_patch16_224

model_dict = {
    'simplecnn': simplecnn,
    'resnet18': resnet18,
    'resnet50': resnet50,
    'vit' : vit_base_patch16_224
}

def create_model(model_name, num_classes):   
    return model_dict[model_name](num_classes = num_classes)
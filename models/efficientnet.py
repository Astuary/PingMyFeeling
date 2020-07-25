from efficientnet_pytorch import EfficientNet

def _efficientnet():
    model = EfficientNet.from_name('efficientnet-b0')
    return model

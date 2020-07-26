import sys
sys.path.append('./models')
from torch import optim, nn
from vgg16 import _vgg
from resnet import _resnet
from efficientnet import _efficientnet
from datasplitter import splits

seed = 42

def train (model, loader, criterion, gpu):
    model.train()
    current_loss = 0
    current_correct = 0
    for train, y_train in iter(loader):
        if gpu:
            train, y_train = train.to('cuda'), y_train.to('cuda')
        optimizer.zero_grad()
        output = model.forward(train)
        _, preds = torch.max(output,1)
        loss = criterion(output, y_train)
        loss.backward()
        optimizer.step()
        current_loss += loss.item()*train.size(0)
        current_correct += torch.sum(preds == y_train.data)
    epoch_loss = current_loss / len(trainLoader.dataset)
    epoch_acc = current_correct.double() / len(trainLoader.dataset)
        
    return epoch_loss, epoch_acc

def validation (model, loader, criterion, gpu):
    model.eval()
    valid_loss = 0
    valid_correct = 0
    for valid, y_valid in iter(loader):
        if gpu:
            valid, y_valid = valid.to('cuda'), y_valid.to('cuda')
        output = model.forward(valid)
        valid_loss += criterion(output, y_valid).item()*valid.size(0)
        equal = (output.max(dim=1)[1] == y_valid.data)
        valid_correct += torch.sum(equal)#type(torch.FloatTensor)
    
    epoch_loss = valid_loss / len(validLoader.dataset)
    epoch_acc = valid_correct.double() / len(validLoader.dataset)
    
    return epoch_loss, epoch_acc

def test (model, loader, gpu):
    model.eval()
    total = 0
    correct = 0 
    count = 0
    #iterating for each sample in the test dataset once
    for test, y_test in iter(loader):
    test, y_test = test.to('cuda'), y_test.to('cuda')
    #Calculate the class probabilities (softmax) for img
    with torch.no_grad():
        output = model.forward(test)
        ps = torch.exp(output)
        _, predicted = torch.max(output.data,1)
        total += y_test.size(0)
        correct += (predicted == y_test).sum().item() 
        count += 1
        print("Accuracy of network on test images is ... {:.4f}....count: {}".format(100*correct/total,  count ))

model = _vgg()
criteria = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr = 0.005, momentum = 0.5)
train_X, val_X, train_y, val_y = splits(seed)

for param in model.parameters():
    param.require_grad = False

epoch_train = 10  
epoch_ctr = 0

if args.gpu:
    model.to('cuda')

for e in range(epoch_train):
    epoch_ctr +=1
    print(epoch_ctr)
    with torch.set_grad_enabled(True):
        epoch_train_loss, epoch_train_acc = train(model, trainLoader, criteria, args.gpu)
    print("Epoch: {} Train Loss : {:.4f}  Train Accuracy: {:.4f}".format(epoch_ctr,epoch_train_loss,epoch_train_acc))
with torch.no_grad():
        epoch_val_loss, epoch_val_acc = validation(model, validLoader, criteria, args.gpu)
    print("Epoch: {} Validation Loss : {:.4f}  Validation Accuracy {:.4f}".format(epoch_ctr,epoch_val_loss,epoch_val_acc))

#test(model, testLoader, args.gpu)
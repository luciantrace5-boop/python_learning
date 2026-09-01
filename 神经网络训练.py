import torch
import torchvision
import torchvision.transforms as transforms
from torchvision.transforms import ToPILImage
import matplotlib.pyplot as plt

show = ToPILImage()
transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
     ])

batch_size = 4

trainset = torchvision.datasets.CIFAR10(root='./dataset', train=True,
                                        download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,
                                          shuffle=True, num_workers=2)

testset = torchvision.datasets.CIFAR10(root='./dataset', train=False,
                                       download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size,
                                         shuffle=False, num_workers=2)
classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

print(len(trainset))
print(trainset[0][0].size())
print(trainset[0][1])
print(classes[trainset[0][1]])
(data, label) = trainset[12]
print(data.size())
print(label)
print(classes[label])

import torch.nn as nn
import torch.nn.functional as F


# 改进后的轻量化现代CNN网络结构
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # 改进1：5×5卷积核→3×3，通道数从6→16，添加padding=1保持尺寸
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(16)  # 改进2：添加批归一化，加速收敛
        # 改进3：第二个卷积核同样改为3×3，通道数从16→32
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(32)
        # 改进4：自适应平均池化，固定输出5×5，避免手动计算尺寸
        self.avgpool = nn.AdaptiveAvgPool2d((5, 5))
        # 全连接层适配新通道数（32×5×5）
        self.fc1 = nn.Linear(32 * 5 * 5, 120)
        self.dropout = nn.Dropout(0.3)  # 改进5：dropout概率从0.5→0.3，平衡防过拟合与特征保留
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # 改进6：卷积→批归一化→激活→池化的现代CNN标准流程
        x = F.max_pool2d(F.relu(self.bn1(self.conv1(x))), 2)
        x = F.max_pool2d(F.relu(self.bn2(self.conv2(x))), 2)
        x = self.avgpool(x)  # 固定输出5×5，适配全连接层输入
        x = x.view(x.size()[0], -1)  # 展平
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


net = Net()
print(net)

from torch import optim

criterion = nn.CrossEntropyLoss()
# 保持原优化器配置，L2正则化（weight_decay=0.001）继续生效
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9, weight_decay=0.001)
num_epochs = 5

train_losses = []


def train(trainloader, net, num_epochs, criterion, optimizer, save_path):
    import os
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for epoch in range(num_epochs):
        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            inputs, labels = data
            optimizer.zero_grad()
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            if i % 1000 == 999:
                avg_loss = running_loss / 1000
                print('epoch %d: batch %5d loss: %.3f' % (epoch + 1, i + 1, avg_loss))
                train_losses.append(avg_loss)
                running_loss = 0.0

        torch.save(net.state_dict(), f"{save_path}/epoch_{epoch + 1}_model.pth")

    print('Finished Training')


save_path = './models'
train(trainloader, net, num_epochs, criterion, optimizer, save_path)


def draw_loss(values):
    plt.figure(figsize=(10, 6))
    plt.plot(values, label='Training Loss')
    plt.title('Training Loss Trend')
    plt.xlabel('Iterations (x1000 batches)')
    plt.ylabel('Average Loss')
    plt.grid(linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()


draw_loss(train_losses)


def predict(testloader, net):
    correct = 0
    total = 0

    with torch.no_grad():
        for data in testloader:
            images, labels = data
            outputs = net(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print('测试集中的准确率为: %d %%' % (100 * correct / total))


predict(testloader, net)
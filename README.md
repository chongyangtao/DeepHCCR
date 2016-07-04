# DeepHCCR
Offline Handwritten Chinese Character Recognition based on GoogLeNet and AlexNet

## Instruction

- Training Data : [*CASIA-HWDB1.0-1.2*](http://www.nlpr.ia.ac.cn/databases/handwriting/Offline_database.html) and [*FlexiFont*](http://www.flexifont.com/flexifont-chn/login/) DataSets (Class = 7354)
- Testing Data : [*Chinese Handwriting Recognition Competition in ICDAR2013*](http://www.nlpr.ia.ac.cn/events/CHRcompetition2013/competition/Home.html) (Class = 3755)
- AlexNet input size is 108 × 108; GoogLeNet input size is 112 × 112
- HCCR-AlexNet Caffemodel can be download from [here](http://pan.baidu.com/s/1bpHT0SZ) 




## Result
- Test accuracy on Chinese Handwriting Recognition Competition in ICDAR2013

|Network|Top-1|Top-2|Top-5|Top-10|
|:---|---|---|---|----
|AlexNet  |0.938437|0.975073|0.990790|0.995370|
|GoogLeNet|0.953227|0.982650|0.993464|0.996728|

-  Test accuracy vs. Iters (GoogLeNet)  
![GoogLeNet](util/Test_Accuracy_GoogLeNet.png "GoogLeNet Test Accuracy")
 
##Reference 
- *Krizhevsky A, Sutskever I, Hinton G E. Imagenet classification with deep convolutional neural networksx[C]//Advances in neural information processing systems. 2012: 1097-1105.*
- *Szegedy C, Liu W, Jia Y, et al. Going deeper with convolutions[C]//Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2015: 1-9.*
- *Zhong Z, Jin L, Xie Z. [High performance offline handwritten Chinese character recognition using GoogLeNet and directional feature maps[C]](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=7333881)//Document Analysis and Recognition (ICDAR), 2015 13th International Conference on. IEEE, 2015: 846-850.*
- *Yin F, Wang Q F, Zhang X Y, et al. ICDAR 2013 Chinese handwriting recognition competition[C]//2013 12th International Conference on Document Analysis and Recognition. IEEE, 2013: 1464-1470.*

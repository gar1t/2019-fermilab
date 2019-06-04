
[Published runs](../README.md)




# mnist_logistic_regression.py



| ID                   | Operation           | Started                  | Time                | Status           | Label                |
| --                   | ---------           | ---------                | ----                | ------           | -----                |
| 10894a20 | mnist_logistic_regression.py | 2019&#8209;06&#8209;04 01:50:39 UTC | 0:00:07 | completed | best |

[run.yml](run.yml)



## Contents

- [Flags](#flags)
- [Scalars](#scalars)
- [Run Files](#run-files)
- [Source Code](#source-code)
- [Output](#output)



## Flags

| Name | Value |
| ---- | ----- |
| batch_size | 128 |
| classes | 10 |
| epochs | 10 |
| input_dim | 784 |
| lr | 0.507665312135 |

[flags.yml](flags.yml)




## Scalars

| Key | Step | Value |
| --- | ---- | ----- |
 | acc | 10 | 0.9261000156402588 |
 | loss | 10 | 0.26600000262260437 |
 | val_acc | 10 | 0.9254999756813049 |
 | val_loss | 10 | 0.2703999876976013 |

[scalars.csv](scalars.csv)




## Run Files

| Path | Type | Size | Modified | MD5 |
| ---- | ---- | ---- | -------- | --- |
| [weights.01-0.3038.hdf5](runfiles/weights.01-0.3038.hdf5) | file | 77.8K | 2019-06-03 20:50:42 UTC | 4f765b57bb5aed17cf19cc81f7fb98f2 |
| [weights.02-0.2980.hdf5](runfiles/weights.02-0.2980.hdf5) | file | 77.8K | 2019-06-03 20:50:42 UTC | b60e4c7e1e0ea4506e59ef6d210bfe91 |
| [weights.03-0.2820.hdf5](runfiles/weights.03-0.2820.hdf5) | file | 77.8K | 2019-06-03 20:50:43 UTC | 79194a79288bdebb212c9a53c5c79215 |
| [weights.04-0.2765.hdf5](runfiles/weights.04-0.2765.hdf5) | file | 77.8K | 2019-06-03 20:50:44 UTC | 626a06fee570c455b39ab8ccebcae828 |
| [weights.05-0.2926.hdf5](runfiles/weights.05-0.2926.hdf5) | file | 77.8K | 2019-06-03 20:50:44 UTC | 2b88c85786ce8fa370eb1af63492d3e4 |
| [weights.06-0.2744.hdf5](runfiles/weights.06-0.2744.hdf5) | file | 77.8K | 2019-06-03 20:50:45 UTC | 5dfc36e72dbd8e8d82b00ada24be70df |
| [weights.07-0.2761.hdf5](runfiles/weights.07-0.2761.hdf5) | file | 77.8K | 2019-06-03 20:50:45 UTC | 5ff578ae008fe6c32434034b3a6d1e36 |
| [weights.08-0.2724.hdf5](runfiles/weights.08-0.2724.hdf5) | file | 77.8K | 2019-06-03 20:50:46 UTC | 98c09d845e2782b89241b6a784a901da |
| [weights.09-0.2720.hdf5](runfiles/weights.09-0.2720.hdf5) | file | 77.8K | 2019-06-03 20:50:47 UTC | 3c65adc37699ca772d9ff56b18757021 |
| [weights.10-0.2704.hdf5](runfiles/weights.10-0.2704.hdf5) | file | 77.8K | 2019-06-03 20:50:47 UTC | 5ac42fc2d35d50ad96776a9ed8f9e55f |

[runfiles.csv](runfiles.csv)




## Source Code

| Path | Size | Modified | MD5 |
| ---- | ---- | -------- | --- |
| [.gitignore](sourcecode/.gitignore) | 33 | 2019-06-03 20:50:39 UTC | c142ba99fc5d2ae336486642974a3bb7 |
| [guild.yml](sourcecode/guild.yml) | 233 | 2019-06-03 20:50:39 UTC | 014c65ee7e76fa8f8451e0d6b724fe83 |
| [mnist_logistic_regression.ipynb](sourcecode/mnist_logistic_regression.ipynb) | 5.9K | 2019-06-03 20:50:39 UTC | e6a74a44be3fff027c5a244d8650a21a |
| [mnist_logistic_regression.py](sourcecode/mnist_logistic_regression.py) | 1.3K | 2019-06-03 20:50:39 UTC | 4ccf3d88cd5c6c79dfbe73cdbf7c676a |
| [mnist_logistic_regression2.ipynb](sourcecode/mnist_logistic_regression2.ipynb) | 5.3K | 2019-06-03 20:50:39 UTC | 3910fa1ec3533bd68b844bab4bbde304 |
| [noisy.ipynb](sourcecode/noisy.ipynb) | 5.9K | 2019-06-03 20:50:39 UTC | bfbde599be9c9de78ee9d1b963fcf803 |
| [runs](sourcecode/runs) | 4.0K | 2019-06-03 20:50:39 UTC |  |
| [runs/trial-1](sourcecode/runs/trial-1) | 4.0K | 2019-06-03 20:50:39 UTC |  |
| [runs/trial-1/flags.yml](sourcecode/runs/trial-1/flags.yml) | 36 | 2019-06-03 20:50:39 UTC | 98913a5d278986b2344c07f41fcc25c3 |

[sourcecode.csv](sourcecode.csv)




## Output

```
Using TensorFlow backend.
WARNING: [tensorflow] From /home/garrett/.local/lib/python2.7/site-packages/tensorflow/python/framework/op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.
Instructions for updating:
Colocations handled automatically by placer.
WARNING: [tensorflow] From /home/garrett/.local/lib/python2.7/site-packages/tensorflow/python/ops/math_ops.py:3066: to_int32 (from tensorflow.python.ops.math_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.cast instead.
Train on 60000 samples, validate on 10000 samples
Epoch 1/10
2019-06-03 20:50:41.634532: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2019-06-03 20:50:41.642767: E tensorflow/stream_executor/cuda/cuda_driver.cc:300] failed call to cuInit: CUDA_ERROR_NO_DEVICE: no CUDA-capable device is detected
2019-06-03 20:50:41.642795: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:161] retrieving CUDA diagnostic information for host: omaha
2019-06-03 20:50:41.642813: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:168] hostname: omaha
2019-06-03 20:50:41.642838: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:192] libcuda reported version is: 410.104.0
2019-06-03 20:50:41.642858: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:196] kernel reported version is: 410.104.0
2019-06-03 20:50:41.642863: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:303] kernel version seems to match DSO: 410.104.0
2019-06-03 20:50:41.644887: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2711940000 Hz
2019-06-03 20:50:41.645256: I tensorflow/compiler/xla/service/service.cc:150] XLA service 0x5e11ae0 executing computations on platform Host. Devices:
2019-06-03 20:50:41.645272: I tensorflow/compiler/xla/service/service.cc:158]   StreamExecutor device (0): <undefined>, <undefined>

  128/60000 [..............................] - ETA: 44s - loss: 2.4413 - acc: 0.0547
 5376/60000 [=>............................] - ETA: 1s - loss: 0.8228 - acc: 0.7608 
10752/60000 [====>.........................] - ETA: 0s - loss: 0.6339 - acc: 0.8173
16256/60000 [=======>......................] - ETA: 0s - loss: 0.5606 - acc: 0.8411
22016/60000 [==========>...................] - ETA: 0s - loss: 0.5171 - acc: 0.8529
27136/60000 [============>.................] - ETA: 0s - loss: 0.4895 - acc: 0.8602
33152/60000 [===============>..............] - ETA: 0s - loss: 0.4645 - acc: 0.8673
39808/60000 [==================>...........] - ETA: 0s - loss: 0.4474 - acc: 0.8720
45952/60000 [=====================>........] - ETA: 0s - loss: 0.4343 - acc: 0.8754
51072/60000 [========================>.....] - ETA: 0s - loss: 0.4246 - acc: 0.8784
56960/60000 [===========================>..] - ETA: 0s - loss: 0.4125 - acc: 0.8818
60000/60000 [==============================] - 1s 11us/step - loss: 0.4073 - acc: 0.8834 - val_loss: 0.3038 - val_acc: 0.9164
Epoch 2/10

  128/60000 [..............................] - ETA: 1s - loss: 0.2844 - acc: 0.9453
 4480/60000 [=>............................] - ETA: 0s - loss: 0.3264 - acc: 0.9125
 9600/60000 [===>..........................] - ETA: 0s - loss: 0.3152 - acc: 0.9140
15360/60000 [======>.......................] - ETA: 0s - loss: 0.3177 - acc: 0.9131
20608/60000 [=========>....................] - ETA: 0s - loss: 0.3131 - acc: 0.9129
25728/60000 [===========>..................] - ETA: 0s - loss: 0.3143 - acc: 0.9122
31616/60000 [==============>...............] - ETA: 0s - loss: 0.3162 - acc: 0.9113
37248/60000 [=================>............] - ETA: 0s - loss: 0.3148 - acc: 0.9115
42752/60000 [====================>.........] - ETA: 0s - loss: 0.3127 - acc: 0.9121
48000/60000 [=======================>......] - ETA: 0s - loss: 0.3138 - acc: 0.9119
53248/60000 [=========================>....] - ETA: 0s - loss: 0.3114 - acc: 0.9124
59008/60000 [============================>.] - ETA: 0s - loss: 0.3095 - acc: 0.9127
60000/60000 [==============================] - 1s 10us/step - loss: 0.3099 - acc: 0.9127 - val_loss: 0.2980 - val_acc: 0.9169
Epoch 3/10

  128/60000 [..............................] - ETA: 1s - loss: 0.2368 - acc: 0.9219
 5888/60000 [=>............................] - ETA: 0s - loss: 0.3037 - acc: 0.9169
11264/60000 [====>.........................] - ETA: 0s - loss: 0.3103 - acc: 0.9149
17152/60000 [=======>......................] - ETA: 0s - loss: 0.3042 - acc: 0.9162
23936/60000 [==========>...................] - ETA: 0s - loss: 0.3017 - acc: 0.9166
30208/60000 [==============>...............] - ETA: 0s - loss: 0.3021 - acc: 0.9160
35968/60000 [================>.............] - ETA: 0s - loss: 0.3000 - acc: 0.9158
41728/60000 [===================>..........] - ETA: 0s - loss: 0.2972 - acc: 0.9166
47488/60000 [======================>.......] - ETA: 0s - loss: 0.2966 - acc: 0.9167
53120/60000 [=========================>....] - ETA: 0s - loss: 0.2954 - acc: 0.9171
58112/60000 [============================>.] - ETA: 0s - loss: 0.2939 - acc: 0.9177
60000/60000 [==============================] - 1s 9us/step - loss: 0.2939 - acc: 0.9179 - val_loss: 0.2820 - val_acc: 0.9195
Epoch 4/10

  128/60000 [..............................] - ETA: 1s - loss: 0.2239 - acc: 0.9453
 5504/60000 [=>............................] - ETA: 0s - loss: 0.2981 - acc: 0.9121
11008/60000 [====>.........................] - ETA: 0s - loss: 0.2950 - acc: 0.9133
16256/60000 [=======>......................] - ETA: 0s - loss: 0.2937 - acc: 0.9142
21120/60000 [=========>....................] - ETA: 0s - loss: 0.2940 - acc: 0.9154
27008/60000 [============>.................] - ETA: 0s - loss: 0.2874 - acc: 0.9182
33280/60000 [===============>..............] - ETA: 0s - loss: 0.2871 - acc: 0.9185
38528/60000 [==================>...........] - ETA: 0s - loss: 0.2857 - acc: 0.9195
43904/60000 [====================>.........] - ETA: 0s - loss: 0.2863 - acc: 0.9197
49664/60000 [=======================>......] - ETA: 0s - loss: 0.2845 - acc: 0.9195
55680/60000 [==========================>...] - ETA: 0s - loss: 0.2863 - acc: 0.9191
60000/60000 [==============================] - 1s 10us/step - loss: 0.2860 - acc: 0.9194 - val_loss: 0.2765 - val_acc: 0.9214
Epoch 5/10

  128/60000 [..............................] - ETA: 1s - loss: 0.2222 - acc: 0.9531
 6144/60000 [==>...........................] - ETA: 0s - loss: 0.2717 - acc: 0.9211
12160/60000 [=====>........................] - ETA: 0s - loss: 0.2689 - acc: 0.9250
17280/60000 [=======>......................] - ETA: 0s - loss: 0.2711 - acc: 0.9237
22784/60000 [==========>...................] - ETA: 0s - loss: 0.2685 - acc: 0.9250
29056/60000 [=============>................] - ETA: 0s - loss: 0.2749 - acc: 0.9239
35584/60000 [================>.............] - ETA: 0s - loss: 0.2765 - acc: 0.9236
40960/60000 [===================>..........] - ETA: 0s - loss: 0.2770 - acc: 0.9236
46336/60000 [======================>.......] - ETA: 0s - loss: 0.2765 - acc: 0.9234
51200/60000 [========================>.....] - ETA: 0s - loss: 0.2759 - acc: 0.9232
56960/60000 [===========================>..] - ETA: 0s - loss: 0.2794 - acc: 0.9224
60000/60000 [==============================] - 1s 9us/step - loss: 0.2801 - acc: 0.9220 - val_loss: 0.2926 - val_acc: 0.9196
Epoch 6/10

  128/60000 [..............................] - ETA: 1s - loss: 0.3511 - acc: 0.9141
 5504/60000 [=>............................] - ETA: 0s - loss: 0.2897 - acc: 0.9201
11520/60000 [====>.........................] - ETA: 0s - loss: 0.2819 - acc: 0.9220
17152/60000 [=======>......................] - ETA: 0s - loss: 0.2809 - acc: 0.9212
22272/60000 [==========>...................] - ETA: 0s - loss: 0.2750 - acc: 0.9224
28032/60000 [=============>................] - ETA: 0s - loss: 0.2727 - acc: 0.9228
34048/60000 [================>.............] - ETA: 0s - loss: 0.2747 - acc: 0.9229
39296/60000 [==================>...........] - ETA: 0s - loss: 0.2751 - acc: 0.9229
44800/60000 [=====================>........] - ETA: 0s - loss: 0.2749 - acc: 0.9230
50432/60000 [========================>.....] - ETA: 0s - loss: 0.2753 - acc: 0.9231
56192/60000 [===========================>..] - ETA: 0s - loss: 0.2750 - acc: 0.9230
60000/60000 [==============================] - 1s 10us/step - loss: 0.2762 - acc: 0.9229 - val_loss: 0.2744 - val_acc: 0.9178
Epoch 7/10

  128/60000 [..............................] - ETA: 1s - loss: 0.2484 - acc: 0.8984
 6016/60000 [==>...........................] - ETA: 0s - loss: 0.2604 - acc: 0.9270
11520/60000 [====>.........................] - ETA: 0s - loss: 0.2723 - acc: 0.9253
17152/60000 [=======>......................] - ETA: 0s - loss: 0.2685 - acc: 0.9262
22144/60000 [==========>...................] - ETA: 0s - loss: 0.2702 - acc: 0.9262
28160/60000 [=============>................] - ETA: 0s - loss: 0.2744 - acc: 0.9241
34048/60000 [================>.............] - ETA: 0s - loss: 0.2748 - acc: 0.9238
39680/60000 [==================>...........] - ETA: 0s - loss: 0.2725 - acc: 0.9241
45312/60000 [=====================>........] - ETA: 0s - loss: 0.2736 - acc: 0.9243
51328/60000 [========================>.....] - ETA: 0s - loss: 0.2736 - acc: 0.9241
55680/60000 [==========================>...] - ETA: 0s - loss: 0.2739 - acc: 0.9239
60000/60000 [==============================] - 1s 10us/step - loss: 0.2730 - acc: 0.9240 - val_loss: 0.2761 - val_acc: 0.9226
Epoch 8/10

  128/60000 [..............................] - ETA: 1s - loss: 0.2088 - acc: 0.9375
 6144/60000 [==>...........................] - ETA: 0s - loss: 0.2675 - acc: 0.9242
12288/60000 [=====>........................] - ETA: 0s - loss: 0.2633 - acc: 0.9254
18048/60000 [========>.....................] - ETA: 0s - loss: 0.2656 - acc: 0.9245
24448/60000 [===========>..................] - ETA: 0s - loss: 0.2639 - acc: 0.9255
30080/60000 [==============>...............] - ETA: 0s - loss: 0.2687 - acc: 0.9246
35712/60000 [================>.............] - ETA: 0s - loss: 0.2721 - acc: 0.9238
41984/60000 [===================>..........] - ETA: 0s - loss: 0.2716 - acc: 0.9242
48128/60000 [=======================>......] - ETA: 0s - loss: 0.2712 - acc: 0.9242
52992/60000 [=========================>....] - ETA: 0s - loss: 0.2714 - acc: 0.9243
58624/60000 [============================>.] - ETA: 0s - loss: 0.2706 - acc: 0.9243
60000/60000 [==============================] - 1s 9us/step - loss: 0.2706 - acc: 0.9243 - val_loss: 0.2724 - val_acc: 0.9225
Epoch 9/10

  128/60000 [..............................] - ETA: 1s - loss: 0.3460 - acc: 0.9062
 5888/60000 [=>............................] - ETA: 0s - loss: 0.2780 - acc: 0.9217
11264/60000 [====>.........................] - ETA: 0s - loss: 0.2765 - acc: 0.9233
17536/60000 [=======>......................] - ETA: 0s - loss: 0.2697 - acc: 0.9248
22400/60000 [==========>...................] - ETA: 0s - loss: 0.2740 - acc: 0.9242
27648/60000 [============>.................] - ETA: 0s - loss: 0.2696 - acc: 0.9248
33280/60000 [===============>..............] - ETA: 0s - loss: 0.2658 - acc: 0.9254
39040/60000 [==================>...........] - ETA: 0s - loss: 0.2691 - acc: 0.9247
45056/60000 [=====================>........] - ETA: 0s - loss: 0.2671 - acc: 0.9254
50304/60000 [========================>.....] - ETA: 0s - loss: 0.2667 - acc: 0.9258
55424/60000 [==========================>...] - ETA: 0s - loss: 0.2687 - acc: 0.9255
60000/60000 [==============================] - 1s 10us/step - loss: 0.2683 - acc: 0.9254 - val_loss: 0.2720 - val_acc: 0.9218
Epoch 10/10

  128/60000 [..............................] - ETA: 1s - loss: 0.2101 - acc: 0.9609
 6016/60000 [==>...........................] - ETA: 0s - loss: 0.2691 - acc: 0.9237
11776/60000 [====>.........................] - ETA: 0s - loss: 0.2624 - acc: 0.9259
17536/60000 [=======>......................] - ETA: 0s - loss: 0.2622 - acc: 0.9255
23168/60000 [==========>...................] - ETA: 0s - loss: 0.2647 - acc: 0.9256
29440/60000 [=============>................] - ETA: 0s - loss: 0.2674 - acc: 0.9252
35072/60000 [================>.............] - ETA: 0s - loss: 0.2686 - acc: 0.9250
40832/60000 [===================>..........] - ETA: 0s - loss: 0.2693 - acc: 0.9254
46464/60000 [======================>.......] - ETA: 0s - loss: 0.2676 - acc: 0.9257
52352/60000 [=========================>....] - ETA: 0s - loss: 0.2675 - acc: 0.9258
57472/60000 [===========================>..] - ETA: 0s - loss: 0.2663 - acc: 0.9260
60000/60000 [==============================] - 1s 9us/step - loss: 0.2660 - acc: 0.9261 - val_loss: 0.2704 - val_acc: 0.9255
```

[output.txt](output.txt)







train_flowers_dataset = train_flowers_dataset.map(process_flower_image)

test_flowers_dataset = test_flowers_dataset.map(process_flower_image)

#let's look at first item

for img, label in train_flowers_dataset.take(1):
  print(label.numpy())
  print(img.numpy())


"""
b'dandelion'
[[[0.18176126 0.03854167 0.02038431]
  [0.1628686  0.02613454 0.01991422]
  [0.17882104 0.03511891 0.02184436]
  ...
  [0.02352941 0.02352941 0.02352941]
  [0.02221297 0.02484586 0.02352941]
  [0.03352769 0.03767329 0.01960784]]

 [[0.19561887 0.04028799 0.02518574]
  [0.2315535  0.05449793 0.014366  ]
  [0.19050245 0.032419   0.02433077]
  ...
  [0.02352941 0.02352941 0.02352941]
  [0.02046569 0.02659314 0.02352941]
  [0.03413469 0.02518478 0.01752643]]

 [[0.1882487  0.04578546 0.02792394]
  [0.1916006  0.03602463 0.01857096]
  [0.16681315 0.03010398 0.02286114]
  ...
  [0.02352941 0.02352941 0.02352941]
  [0.02046569 0.02659314 0.02352941]
  [0.02120098 0.02189223 0.02154661]]

 ...

 [[0.3543237  0.24676968 0.28330365]
  [0.2734375  0.18658088 0.2779718 ]
  [0.31186906 0.2234375  0.27206552]
  ...
  [0.02017176 0.02688706 0.0233207 ]
  [0.01236309 0.02425992 0.02092046]
  [0.02217276 0.02217276 0.01820715]]

 [[0.35637447 0.2149481  0.31130323]
  [0.34208983 0.26657763 0.3288823 ]
  [0.33434626 0.26779544 0.3031767 ]
  ...
  [0.02352941 0.02352941 0.02352941]
  [0.01958008 0.02135129 0.02046569]
  [0.02646676 0.02193628 0.01841203]]

 [[0.35267788 0.26049134 0.3344181 ]
  [0.29791668 0.21360102 0.29273897]
  [0.32072324 0.24241057 0.28353822]
  ...
  [0.0233542  0.0235993  0.01587871]
  [0.01917701 0.02438726 0.01393899]
  [0.0314951  0.02352941 0.01409314]]]
"""

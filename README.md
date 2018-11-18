# duckiestuff

Data and config files needed to train YOLO with Duckie images. You will need to modify all paths in <code>train.txt</code> and <code>dataset_images_203.txt</code> (simple find and replace) in the txt files according to your working directory.

Created the <code>train.txt</code> file with: <code>cat  dataset_images_201.txt dataset_images_202.txt > train.txt</code>. Using <code>dataset_images_203.txt</code> as the test set.

It is meant to be executed as <code>./darknet detector train cfg/duckie.data ../duckiestuff/cfg/yolov3-duckie.cfg darknet53.conv/74</code>

For this to work, we need to copy the file <code>duckie.data</code> to the <code>cfg</code> directory inside the directory <code>darknet</code> after modifying the paths. Also, we need to copy the file <code>duckie.names</code> to the <code>data</code> directory inside the directory <code>darknet</code>.

We also need to create a directory named <code>duckie_backup</code> inside the directory <code>darknet</code>.

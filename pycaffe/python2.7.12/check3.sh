#!/bin/sh

echo 'check.py�μ¹�'

ipython2 ./value3/check_china_lenet.py > ./log/china_lenet_value3_miss_num.txt

ipython2 ./value3/check_china_lenet_gap.py > ./log/china_lenet_gap_value3_miss_num.txt

ipython2 ./value3/check_china_lenet_dp2.py > ./log/china_lenet_dp2_value3_miss_num.txt

ipython2 ./value3/check_china_lenet_dp2_gap.py > ./log/china_lenet_dp2_gap_value3_miss_num.txt

ipython2 ./value3/check_china_lenet_dp23.py > ./log/china_lenet_dp23_value3_miss_num.txt

ipython2 ./value3/check_china_lenet_dp234.py > ./log/china_lenet_dp234_value3_miss_num.txt

echo 'check.py��λ'

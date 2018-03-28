package com;

/**
 * @Time : 2018/2/23 no 下午3:32
 * @USER : vvguoliang
 * @File : Sort.java
 * @Software: IntelliJ IDEA
 * code is far away from bugs with the god animal protecting
 * I love animals. They taste delicious.
 * ***┏┓   ┏ ┓
 * **┏┛┻━━━┛ ┻┓
 * **┃   ☃   ┃
 * **┃ ┳┛  ┗┳ ┃
 * **┃    ┻   ┃
 * **┗━┓    ┏━┛
 * ****┃    ┗━━━┓
 * ****┃ 神兽保佑 ┣┓
 * ****┃ 永无BUG！┏┛
 * ****┗┓┓┏━┳┓┏┛┏┛
 * ******┃┫┫  ┃┫┫
 * ******┗┻┛  ┗┻┛
 */
public class Sort {
    /**
     * 插入排序—直接插入排序(Straight Insertion Sort)
     * <p/>
     * 对代码进行优化（时间复杂度O(n^2)）
     * <p/>
     * 效率：
     * 时间复杂度：O（n^2）.
     * 其他的插入排序有二分插入排序，2-路插入排序。
     */

    public static void insertion_sort(int[] a) {
        for (int i = 0; i < a.length; i++) {
            int j;
            int x = a[i];
            for (j = i; j > 0 && x < a[j - 1]; j--) {
                a[j] = a[j - 1];
            }
            a[j] = x;
        }
        print(a, 1);
    }

    /**
     * 希尔排序（Shell`s Sort）
     */

    public static void shellSortSmallToBig(int[] data) {
        int j;
        int temp;
        for (int increment = data.length / 2; increment > 0; increment /= 2) {
//            System.out.println("increment:" + increment);
            for (int i = increment; i < data.length; i++) {
                // System.out.println("i:" + i);
                temp = data[i];
                for (j = i - increment; j >= 0; j -= increment) {
                    // System.out.println("j:" + j);
                    // System.out.println("temp:" + temp);
                    // System.out.println("data[" + j + "]:" + data[j]);
                    if (temp < data[j]) {
                        data[j + increment] = data[j];
                    } else {
                        break;
                    }
                }
                data[j + increment] = temp;
            }
        }
        print(data, 1);
    }

    /**
     * 选择排序—简单选择排序（Simple Selection Sort）
     */

    public static void SimpleSelectionSort(int[] arr) {
        //选择排序的优化
        for (int i = 0; i < arr.length - 1; i++) {// 做第i趟排序
            int k = i;
            for (int j = k + 1; j < arr.length; j++) {// 选最小的记录
                if (arr[j] < arr[k]) {
                    k = j; //记下目前找到的最小值所在的位置
                }
            }
            //在内层循环结束，也就是找到本轮循环的最小的数以后，再进行交换
            if (i != k) {  //交换a[i]和a[k]
                int temp = arr[i];
                arr[i] = arr[k];
                arr[k] = temp;
            }
        }
        print(arr, 1);
    }

    /**
     * 堆排序（Heap Sort）
     */
//构建大根堆：将array看成完全二叉树的顺序存储结构
    private static int[] buildMaxHeap(int[] array) {
        //从最后一个节点array.length-1的父节点（array.length-1-1）/2开始，直到根节点0，反复调整堆
        for (int i = (array.length - 2) / 2; i >= 0; i--) {
            adjustDownToUp(array, i, array.length);
        }
        return array;
    }

    //将元素array[k]自下往上逐步调整树形结构
    private static void adjustDownToUp(int[] array, int k, int length) {
        int temp = array[k];
        for (int i = 2 * k + 1; i < length - 1; i = 2 * i + 1) {    //i为初始化为节点k的左孩子，沿节点较大的子节点向下调整
            if (i < length && array[i] < array[i + 1]) {  //取节点较大的子节点的下标
                i++;   //如果节点的右孩子>左孩子，则取右孩子节点的下标
            }
            if (temp >= array[i]) {  //根节点 >=左右子女中关键字较大者，调整结束
                break;
            } else {   //根节点 <左右子女中关键字较大者
                array[k] = array[i];  //将左右子结点中较大值array[i]调整到双亲节点上
                k = i; //【关键】修改k值，以便继续向下调整
            }
        }
    }

    //堆排序
    public static int[] heapSort(int[] array) {
        array = buildMaxHeap(array); //初始建堆，array[0]为第一趟值最大的元素
        for (int i = array.length - 1; i > 1; i--) {
            int temp = array[0];  //将堆顶元素和堆低元素交换，即得到当前最大元素正确的排序位置
            array[0] = array[i];
            array[i] = temp;
            adjustDownToUp(array, 0, i);  //整理，将剩余的元素整理成堆
        }
        return array;
    }


    /**
     * 冒泡排序（Bubble Sort）
     */

    public static void Bubble_Sort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {//外层循环控制排序趟数
            for (int j = 0; j < arr.length - 1 - i; j++) {//内层循环控制每一趟排序多少次
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
        print(arr, 1);
    }

    /**
     * 快速排序（Quick Sort）
     */
    public static void Quicksort(int[] a, int low, int high) {
        int start = low;
        int end = high;
        int key = a[low];

        while (end > start) {
            //从后往前比较
            while (end > start && a[end] >= key)  //如果没有比关键值小的，比较下一个，直到有比关键值小的交换位置，然后又从前往后比较
                end--;
            if (a[end] <= key) {
                int temp = a[end];
                a[end] = a[start];
                a[start] = temp;
            }
            //从前往后比较
            while (end > start && a[start] <= key)//如果没有比关键值大的，比较下一个，直到有比关键值大的交换位置
                start++;
            if (a[start] >= key) {
                int temp = a[start];
                a[start] = a[end];
                a[end] = temp;
            }
            //此时第一次循环比较结束，关键值的位置已经确定了。左边的值都比关键值小，右边的值都比关键值大，但是两边的顺序还有可能是不一样的，进行下面的递归调用
        }
        //递归
        if (start > low) Quicksort(a, low, start - 1);//左边序列。第一个索引位置到关键值索引-1
        if (end < high) Quicksort(a, end + 1, high);//右边序列。从关键值索引+1到最后一个
    }

    /**
     * 归并排序（Merge Sort）
     */
    public static int[] Mergesort(int[] a, int low, int high) {
        int mid = (low + high) / 2;
        if (low < high) {
            Mergesort(a, low, mid);
            Mergesort(a, mid + 1, high);
            //左右归并
            merge(a, low, mid, high);
        }
        return a;
    }

    public static void merge(int[] a, int low, int mid, int high) {
        int[] temp = new int[high - low + 1];
        int i = low;
        int j = mid + 1;
        int k = 0;
        // 把较小的数先移到新数组中
        while (i <= mid && j <= high) {
            if (a[i] < a[j]) {
                temp[k++] = a[i++];
            } else {
                temp[k++] = a[j++];
            }
        }
        // 把左边剩余的数移入数组
        while (i <= mid) {
            temp[k++] = a[i++];
        }
        // 把右边边剩余的数移入数组
        while (j <= high) {
            temp[k++] = a[j++];
        }
        // 把新数组中的数覆盖nums数组
        for (int x = 0; x < temp.length; x++) {
            a[x + low] = temp[x];
        }
    }

    /**
     * 桶排序/基数排序(Radix Sort)
     */
    public static int getMax(int[] values) {
        int tmp = Integer.MIN_VALUE;
        if (null != values) {
            tmp = values[0];
            for (int value : values) {
                if (tmp < value) {
                    tmp = value;
                }
            }
        }
        return tmp;
    }

    //桶式排序函数
    //a是要排序的数组
    //max是最大数字（这里我们默认数字最小为0）
    public static void Radixsort(int[] a, int max) {
        //声明一个数组，这就是桶，编号从0到max的桶，一共max+1个
        int[] count = new int[max + 1];
        //遍历数组，用桶计数
        for (int i = 0; i < a.length; i++) {
            count[a[i]]++;
        }
        //将桶里面的数字倒出
        for (int i = 0; i < max + 1; i++) {
            while (count[i] > 0) {
                System.out.print(i + " ");
                count[i]--;
            }
        }
    }

    public static void print(int a[], int type) {
        String type_string = "\n";
        if (type == 0) {
            for (int anA : a) {
                type_string += anA + " ";
            }
        } else {
            for (int anA : a) {
                type_string += anA + " ";
            }
        }
        System.out.println(type_string);
    }

    public static void main(String[] args) {
        int lists[] = {5, 67, 8, 9, 4, 3, 6, 88, 9, 4, 6, 34, 34, 2, 6, 7, 8, 9, 9, 90, 4, 3, 6, 7, 2};
        print(lists, 0);
//        insertion_sort(lists);   //插入排序—直接插入排序
//        shellSortSmallToBig(lists);  //希尔排序
//        SimpleSelectionSort(lists);  ///选择排序
//        print(heapSort(lists), 1); //堆排序
//        Bubble_Sort(lists);  //冒泡排序
//        Quicksort(lists, 0, lists.length - 1);   //快速排序
//        print(lists, 1);
//        print(Mergesort(lists, 0, lists.length - 1), 1); //归并排序
//        int max = getMax(lists);
//        Radixsort(lists, max);  //桶排序/基数排序
    }
}

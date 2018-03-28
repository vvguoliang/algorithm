# algorithm
排序算法python和java
<div class="post">
<h1 class="postTitle">
<a class="postTitle2" href="http://www.cnblogs.com/woider/p/6835466.html" id="cb_post_title_url">Python 八大排序算法速度比较</a>
</h1>
<div class="clear"></div>
<div class="postBody">
<div class="blogpost-body" id="cnblogs_post_body"><blockquote>
<p>这篇文章并不是介绍排序算法原理的，纯粹是想比较一下各种排序算法在真实场景下的运行速度。</p>
<p>算法由 Python 实现，用到了一些语法糖，可能会和其他语言有些区别，仅当参考就好。</p>
<p>测试的数据是自动生成的，以数组形式保存到文件中，保证数据源的一致性。</p>
</blockquote>
<p> </p>
<h2>排序算法</h2>
<p><img alt="" src="https://images2015.cnblogs.com/blog/875028/201705/875028-20170510125950801-1225042288.png"/></p>
<p> </p>
<h3>直接插入排序</h3>
<ul>
<li>时间复杂度：O(n²)</li>
<li>空间复杂度：O(1)</li>
<li>稳定性：稳定</li>
</ul>
<div class="cnblogs_code">
<pre><span style="color: #0000ff">def</span><span style="color: #000000"> insert_sort(array):
    </span><span style="color: #0000ff">for</span> i <span style="color: #0000ff">in</span><span style="color: #000000"> range(len(array)):
        </span><span style="color: #0000ff">for</span> j <span style="color: #0000ff">in</span><span style="color: #000000"> range(i):
            </span><span style="color: #0000ff">if</span> array[i] &lt;<span style="color: #000000"> array[j]:
                array.insert(j, array.pop(i))
                </span><span style="color: #0000ff">break</span>
    <span style="color: #0000ff">return</span> array</pre>
</div>
<p> </p>
<h3>希尔排序</h3>
<ul>
<li>时间复杂度：O(n)</li>
<li>空间复杂度：O(n√n)</li>
<li>稳定性：不稳定</li>
</ul>
<div class="cnblogs_code">
<pre><span style="color: #0000ff">def</span><span style="color: #000000"> shell_sort(array):
    gap </span>=<span style="color: #000000"> len(array)
    </span><span style="color: #0000ff">while</span> gap &gt; 1<span style="color: #000000">:
        gap </span>= gap // 2
        <span style="color: #0000ff">for</span> i <span style="color: #0000ff">in</span><span style="color: #000000"> range(gap, len(array)):
            </span><span style="color: #0000ff">for</span> j <span style="color: #0000ff">in</span> range(i %<span style="color: #000000"> gap, i, gap):
                </span><span style="color: #0000ff">if</span> array[i] &lt;<span style="color: #000000"> array[j]:
                    array[i], array[j] </span>=<span style="color: #000000"> array[j], array[i]
    </span><span style="color: #0000ff">return</span> array</pre>
</div>
<p> </p>
<h3>简单选择排序</h3>
<ul>
<li>时间复杂度：O(n²)</li>
<li>空间复杂度：O(1)</li>
<li>稳定性：不稳定</li>
</ul>
<div class="cnblogs_code">
<pre><span style="color: #0000ff">def</span><span style="color: #000000"> select_sort(array):
    </span><span style="color: #0000ff">for</span> i <span style="color: #0000ff">in</span><span style="color: #000000"> range(len(array)):
        x </span>= i  <span style="color: #008000">#</span><span style="color: #008000"> min index</span>
        <span style="color: #0000ff">for</span> j <span style="color: #0000ff">in</span><span style="color: #000000"> range(i, len(array)):
            </span><span style="color: #0000ff">if</span> array[j] &lt;<span style="color: #000000"> array[x]:
                x </span>=<span style="color: #000000"> j
        array[i], array[x] </span>=<span style="color: #000000"> array[x], array[i]
    </span><span style="color: #0000ff">return</span> array</pre>
</div>
<p> </p>
<h3>堆排序</h3>
<ul>
<li>时间复杂度：O(nlog₂n)</li>
<li>空间复杂度：O(1)</li>
<li>稳定性：不稳定</li>
</ul>
<div class="cnblogs_code">
<pre><span style="color: #0000ff">def</span><span style="color: #000000"> heap_sort(array):
    </span><span style="color: #0000ff">def</span><span style="color: #000000"> heap_adjust(parent):
        child </span>= 2 * parent + 1  <span style="color: #008000">#</span><span style="color: #008000"> left child</span>
        <span style="color: #0000ff">while</span> child &lt;<span style="color: #000000"> len(heap):
            </span><span style="color: #0000ff">if</span> child + 1 &lt;<span style="color: #000000"> len(heap):
                </span><span style="color: #0000ff">if</span> heap[child + 1] &gt;<span style="color: #000000"> heap[child]:
                    child </span>+= 1  <span style="color: #008000">#</span><span style="color: #008000"> right child</span>
            <span style="color: #0000ff">if</span> heap[parent] &gt;=<span style="color: #000000"> heap[child]:
                </span><span style="color: #0000ff">break</span><span style="color: #000000">
            heap[parent], heap[child] </span>=<span style="color: #000000"> \
                heap[child], heap[parent]
            parent, child </span>= child, 2 * child + 1<span style="color: #000000">

    heap, array </span>=<span style="color: #000000"> array.copy(), []
    </span><span style="color: #0000ff">for</span> i <span style="color: #0000ff">in</span> range(len(heap) // 2, -1, -1<span style="color: #000000">):
        heap_adjust(i)
    </span><span style="color: #0000ff">while</span> len(heap) !=<span style="color: #000000"> 0:
        heap[0], heap[</span>-1] = heap[-1<span style="color: #000000">], heap[0]
        array.insert(0, heap.pop())
        heap_adjust(0)
    </span><span style="color: #0000ff">return</span> array</pre>
</div>
<p> </p>
<h3>冒泡排序</h3>
<ul>
<li>时间复杂度：O(n²)</li>
<li>空间复杂度：O(1)</li>
<li>稳定性：稳定</li>
</ul>
<div class="cnblogs_code">
<pre><span style="color: #0000ff">def</span><span style="color: #000000"> bubble_sort(array):
    </span><span style="color: #0000ff">for</span> i <span style="color: #0000ff">in</span><span style="color: #000000"> range(len(array)):
        </span><span style="color: #0000ff">for</span> j <span style="color: #0000ff">in</span><span style="color: #000000"> range(i, len(array)):
            </span><span style="color: #0000ff">if</span> array[i] &gt;<span style="color: #000000"> array[j]:
                array[i], array[j] </span>=<span style="color: #000000"> array[j], array[i]
    </span><span style="color: #0000ff">return</span> array</pre>
</div>
<p> </p>
<h3>快速排序</h3>
<ul>
<li>时间复杂度：O(nlog₂n)</li>
<li>空间复杂度：O(nlog₂n)</li>
<li>稳定性：不稳定</li>
</ul>
<div class="cnblogs_code">
<pre><span style="color: #0000ff">def</span><span style="color: #000000"> quick_sort(array):
    </span><span style="color: #0000ff">def</span><span style="color: #000000"> recursive(begin, end):
        </span><span style="color: #0000ff">if</span> begin &gt;<span style="color: #000000"> end:
            </span><span style="color: #0000ff">return</span><span style="color: #000000">
        l, r </span>=<span style="color: #000000"> begin, end
        pivot </span>=<span style="color: #000000"> array[l]
        </span><span style="color: #0000ff">while</span> l &lt;<span style="color: #000000"> r:
            </span><span style="color: #0000ff">while</span> l &lt; r <span style="color: #0000ff">and</span> array[r] &gt;<span style="color: #000000"> pivot:
                r </span>-= 1
            <span style="color: #0000ff">while</span> l &lt; r <span style="color: #0000ff">and</span> array[l] &lt;=<span style="color: #000000"> pivot:
                l </span>+= 1<span style="color: #000000">
            array[l], array[r] </span>=<span style="color: #000000"> array[r], array[l]
        array[l], array[begin] </span>=<span style="color: #000000"> pivot, array[l]
        recursive(begin, l </span>- 1<span style="color: #000000">)
        recursive(r </span>+ 1<span style="color: #000000">, end)

    recursive(0, len(array) </span>- 1<span style="color: #000000">)
    </span><span style="color: #0000ff">return</span> array</pre>
</div>
<p> </p>
<h3>归并排序</h3>
<ul>
<li>时间复杂度：O(nlog₂n)</li>
<li>空间复杂度：O(1)</li>
<li>稳定性：稳定</li>
</ul>
<div class="cnblogs_code">
<pre><span style="color: #0000ff">def</span><span style="color: #000000"> merge_sort(array):
    </span><span style="color: #0000ff">def</span><span style="color: #000000"> merge_arr(arr_l, arr_r):
        array </span>=<span style="color: #000000"> []
        </span><span style="color: #0000ff">while</span> len(arr_l) <span style="color: #0000ff">and</span><span style="color: #000000"> len(arr_r):
            </span><span style="color: #0000ff">if</span> arr_l[0] &lt;=<span style="color: #000000"> arr_r[0]:
                array.append(arr_l.pop(0))
            </span><span style="color: #0000ff">elif</span> arr_l[0] &gt;<span style="color: #000000"> arr_r[0]:
                array.append(arr_r.pop(0))
        </span><span style="color: #0000ff">if</span> len(arr_l) !=<span style="color: #000000"> 0:
            array </span>+=<span style="color: #000000"> arr_l
        </span><span style="color: #0000ff">elif</span> len(arr_r) !=<span style="color: #000000"> 0:
            array </span>+=<span style="color: #000000"> arr_r
        </span><span style="color: #0000ff">return</span><span style="color: #000000"> array

    </span><span style="color: #0000ff">def</span><span style="color: #000000"> recursive(array):
        </span><span style="color: #0000ff">if</span> len(array) == 1<span style="color: #000000">:
            </span><span style="color: #0000ff">return</span><span style="color: #000000"> array
        mid </span>= len(array) // 2<span style="color: #000000">
        arr_l </span>=<span style="color: #000000"> recursive(array[:mid])
        arr_r </span>=<span style="color: #000000"> recursive(array[mid:])
        </span><span style="color: #0000ff">return</span><span style="color: #000000"> merge_arr(arr_l, arr_r)

    </span><span style="color: #0000ff">return</span> recursive(array)</pre>
</div>
<p> </p>
<h3>基数排序</h3>
<ul>
<li>时间复杂度：O(d(r+n))</li>
<li>空间复杂度：O(rd+n)</li>
<li>稳定性：稳定</li>
</ul>
<div class="cnblogs_code">
<pre><span style="color: #0000ff">def</span><span style="color: #000000"> radix_sort(array):
    bucket, digit </span>=<span style="color: #000000"> [[]], 0
    </span><span style="color: #0000ff">while</span> len(bucket[0]) !=<span style="color: #000000"> len(array):
        bucket </span>=<span style="color: #000000"> [[], [], [], [], [], [], [], [], [], []]
        </span><span style="color: #0000ff">for</span> i <span style="color: #0000ff">in</span><span style="color: #000000"> range(len(array)):
            num </span>= (array[i] // 10 ** digit) % 10<span style="color: #000000">
            bucket[num].append(array[i])
        array.clear()
        </span><span style="color: #0000ff">for</span> i <span style="color: #0000ff">in</span><span style="color: #000000"> range(len(bucket)):
            array </span>+=<span style="color: #000000"> bucket[i]
        digit </span>+= 1
    <span style="color: #0000ff">return</span> array</pre>
</div>
<p> </p>
<h2>速度比较</h2>
<div class="cnblogs_code"><img alt="" class="code_img_closed" id="code_img_closed_07957f0c-4cae-4423-8f34-18b89a24af1b" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif"/><img alt="" class="code_img_opened" id="code_img_opened_07957f0c-4cae-4423-8f34-18b89a24af1b" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" style="display: none"/>
<div class="cnblogs_code_hide" id="cnblogs_code_open_07957f0c-4cae-4423-8f34-18b89a24af1b">
<pre><span style="color: #0000ff">from</span> random <span style="color: #0000ff">import</span><span style="color: #000000"> random
</span><span style="color: #0000ff">from</span> json <span style="color: #0000ff">import</span><span style="color: #000000"> dumps, loads


</span><span style="color: #008000">#</span><span style="color: #008000"> 生成随机数文件</span>
<span style="color: #0000ff">def</span> dump_random_array(file=<span style="color: #800000">'</span><span style="color: #800000">numbers.json</span><span style="color: #800000">'</span>, size=10 ** 4<span style="color: #000000">):
    fo </span>= open(file, <span style="color: #800000">'</span><span style="color: #800000">w</span><span style="color: #800000">'</span>, 1024<span style="color: #000000">)
    numlst </span>=<span style="color: #000000"> list()
    </span><span style="color: #0000ff">for</span> i <span style="color: #0000ff">in</span><span style="color: #000000"> range(size):
        numlst.append(int(random() </span>* 10 ** 10<span style="color: #000000">))
    fo.write(dumps(numlst))
    fo.close()


</span><span style="color: #008000">#</span><span style="color: #008000"> 加载随机数列表</span>
<span style="color: #0000ff">def</span> load_random_array(file=<span style="color: #800000">'</span><span style="color: #800000">numbers.json</span><span style="color: #800000">'</span><span style="color: #000000">):
    fo </span>= open(file, <span style="color: #800000">'</span><span style="color: #800000">r</span><span style="color: #800000">'</span>, 1024<span style="color: #000000">)
    </span><span style="color: #0000ff">try</span><span style="color: #000000">:
        numlst </span>=<span style="color: #000000"> fo.read()
    </span><span style="color: #0000ff">finally</span><span style="color: #000000">:
        fo.close()
    </span><span style="color: #0000ff">return</span> loads(numlst)</pre>
</div>
<span class="cnblogs_code_collapse">数据生成函数</span></div>
<div class="cnblogs_code"><img alt="" class="code_img_closed" id="code_img_closed_7e337240-15d1-4995-a143-dd8592dc05dd" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif"/><img alt="" class="code_img_opened" id="code_img_opened_7e337240-15d1-4995-a143-dd8592dc05dd" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" style="display: none"/>
<div class="cnblogs_code_hide" id="cnblogs_code_open_7e337240-15d1-4995-a143-dd8592dc05dd">
<pre><span style="color: #0000ff">from</span> _datetime <span style="color: #0000ff">import</span><span style="color: #000000"> datetime


</span><span style="color: #008000">#</span><span style="color: #008000"> 显示函数执行时间</span>
<span style="color: #0000ff">def</span><span style="color: #000000"> exectime(func):
    </span><span style="color: #0000ff">def</span> inner(*args, **<span style="color: #000000">kwargs):
        begin </span>=<span style="color: #000000"> datetime.now()
        result </span>= func(*args, **<span style="color: #000000">kwargs)
        end </span>=<span style="color: #000000"> datetime.now()
        inter </span>= end -<span style="color: #000000"> begin
        </span><span style="color: #0000ff">print</span>(<span style="color: #800000">'</span><span style="color: #800000">E-time:{0}.{1}</span><span style="color: #800000">'</span><span style="color: #000000">.format(
            inter.seconds,
            inter.microseconds
        ))
        </span><span style="color: #0000ff">return</span><span style="color: #000000"> result

    </span><span style="color: #0000ff">return</span> inner</pre>
</div>
<span class="cnblogs_code_collapse">显示执行时间</span></div>
<p><strong>如果数据量特别大，采用分治算法的快速排序和归并排序，可能会出现递归层次超出限制的错误。</strong></p>
<p>解决办法：导入 sys 模块（import sys），设置最大递归次数（sys.setrecursionlimit(10 ** 8)）。</p>
<div class="cnblogs_code">
<pre><span style="color: #000000">@exectime
</span><span style="color: #0000ff">def</span><span style="color: #000000"> bubble_sort(array):
    </span><span style="color: #0000ff">for</span> i <span style="color: #0000ff">in</span><span style="color: #000000"> range(len(array)):
        </span><span style="color: #0000ff">for</span> j <span style="color: #0000ff">in</span><span style="color: #000000"> range(i, len(array)):
            </span><span style="color: #0000ff">if</span> array[i] &gt;<span style="color: #000000"> array[j]:
                array[i], array[j] </span>=<span style="color: #000000"> array[j], array[i]
    </span><span style="color: #0000ff">return</span><span style="color: #000000"> array


array </span>=<span style="color: #000000"> load_random_array()
</span><span style="color: #0000ff">print</span>(bubble_sort(array) == sorted(array))</pre>
</div>
<p><span style="font-size: 12px; color: #888888">↑ 示例：测试直接插入排序算法的运行时间，@exectime 为执行时间装饰器。</span></p>
<h3>算法执行时间</h3>
<p><img alt="" src="https://images2015.cnblogs.com/blog/875028/201705/875028-20170510234041066-399934425.png"/></p>
<h3>算法速度比较</h3>
<p><img alt="" src="https://images2015.cnblogs.com/blog/875028/201705/875028-20170511003402707-2055171743.png"/></p>
<p><img alt="" src="https://images2015.cnblogs.com/blog/875028/201705/875028-20170511000356644-56652327.png"/></p>
<p> </p></div><div id="MySignature"></div>
<div class="clear"></div>
<div id="blog_post_info_block">
<div id="BlogPostCategory"></div>
<div id="EntryTag"></div>
<div id="blog_post_info">
</div>
<div class="clear"></div>
<div id="post_next_prev"></div>
</div>
</div>
</div>


<div class="post">
<h1 class="postTitle">
<a class="postTitle2" href="http://www.cnblogs.com/10158wsj/p/6782124.html" id="cb_post_title_url">Java常用的八种排序算法与代码实现</a>
</h1>
<div class="clear"></div>
<div class="postBody">
<div class="blogpost-body" id="cnblogs_post_body"><p><span style="font-size: 16px"><strong>排序问题一直是程序员工作与面试的重点，今天特意整理研究下与大家共勉！这里列出8种常见的经典排序，基本涵盖了所有的排序算法。</strong></span></p>
<h1>1.直接插入排序</h1>
<p><span style="font-size: 16px">      我们经常会到这样一类排序问题：把新的数据插入到已经排好的数据列中。将第一个数和第二个数排序，然后构成一个有序序列将第三个数插入进去，构成一个新的有序序列。</span><span style="font-size: 16px">对第四个数、第五个数……直到最后一个数，重复第二步。如题所示：</span></p>
<p><span style="font-size: 16px"><img alt="" height="389" src="https://images2015.cnblogs.com/blog/1153367/201704/1153367-20170428142931803-787524153.png" width="478"/></span></p>
<p><span style="font-size: 16px">直接插入排序（Straight Insertion Sorting）的基本思想：在要排序的一组数中，假设前面(n-1) [n&gt;=2] 个数已经是排好顺序的，现在要把第n个数插到前面的有序数中，使得这n个数也是排好顺序的。如此反复循环，直到全部排好顺序。</span></p>
<p><span style="font-size: 16px"><strong>代码实现：</strong></span></p>
<p><span style="font-size: 16px">首先设定插入次数，即循环次数，for(int i=1;i&lt;length;i++)，1个数的那次不用插入。</span></p>
<p><span style="font-size: 16px">设定插入数和得到已经排好序列的最后一个数的位数。insertNum和j=i-1。</span></p>
<p><span style="font-size: 16px">从最后一个数开始向前循环，如果插入数小于当前数，就将当前数向后移动一位。</span></p>
<p><span style="font-size: 16px">将当前数放置到空着的位置，即j+1。</span></p>
<p><span style="font-size: 16px">代码如下：</span></p>
<div class="cnblogs_code">
<pre><span style="color: #008080"> 1</span> <span style="color: #0000ff">public</span> <span style="color: #0000ff">void</span> insertSort(<span style="color: #0000ff">int</span><span style="color: #000000"> [] a){
</span><span style="color: #008080"> 2</span>         <span style="color: #0000ff">int</span> len=a.length;<span style="color: #008000">//</span><span style="color: #008000">单独把数组长度拿出来，提高效率</span>
<span style="color: #008080"> 3</span>         <span style="color: #0000ff">int</span> insertNum;<span style="color: #008000">//</span><span style="color: #008000">要插入的数</span>
<span style="color: #008080"> 4</span>         <span style="color: #0000ff">for</span>(<span style="color: #0000ff">int</span> i=1;i&lt;len;i++){<span style="color: #008000">//</span><span style="color: #008000">因为第一次不用，所以从1开始</span>
<span style="color: #008080"> 5</span>             insertNum=<span style="color: #000000">a[i];
</span><span style="color: #008080"> 6</span>             <span style="color: #0000ff">int</span> j=i-1;<span style="color: #008000">//</span><span style="color: #008000">序列元素个数</span>
<span style="color: #008080"> 7</span>             <span style="color: #0000ff">while</span>(j&gt;0&amp;&amp;a[j]&gt;insertNum){<span style="color: #008000">//</span><span style="color: #008000">从后往前循环，将大于insertNum的数向后移动</span>
<span style="color: #008080"> 8</span>                 a[j+1]=a[j];<span style="color: #008000">//</span><span style="color: #008000">元素向后移动</span>
<span style="color: #008080"> 9</span>                 j--<span style="color: #000000">;
</span><span style="color: #008080">10</span> <span style="color: #000000">            }
</span><span style="color: #008080">11</span>             a[j+1]=insertNum;<span style="color: #008000">//</span><span style="color: #008000">找到位置，插入当前元素</span>
<span style="color: #008080">12</span> <span style="color: #000000">        }
</span><span style="color: #008080">13</span>     }</pre>
</div>
<h1>2.希尔排序</h1>
<p><span style="font-size: 16px">      针对直接插入排序的下效率问题，有人对次进行了改进与升级，这就是现在的希尔排序。<strong>希尔排序</strong>，也称<strong>递减增量排序算法</strong>，是插入排序的一种更高效的改进版本。希尔排序是非稳定排序算法。</span></p>
<p><span style="font-size: 16px">希尔排序是基于插入排序的以下两点性质而提出改进方法的：</span></p>
<ul>
<li><span style="font-size: 16px">插入排序在对几乎已经排好序的数据操作时， 效率高， 即可以达到线性排序的效率</span></li>
<li><span style="font-size: 16px">但插入排序一般来说是低效的， 因为插入排序每次只能将数据移动一位</span></li>
</ul>
<p><span style="font-size: 16px">如图所示：</span></p>
<p><img alt="" src="https://images2015.cnblogs.com/blog/1153367/201704/1153367-20170428150738928-1745428645.png"/></p>
<p><span style="font-size: 16px">对于直接插入排序问题，数据量巨大时。</span></p>
<p><span style="font-size: 16px">将数的个数设为n，取奇数k=n/2，将下标差值为k的数分为一组，构成有序序列。</span></p>
<p><span style="font-size: 16px">再取k=k/2 ，将下标差值为k的书分为一组，构成有序序列。</span></p>
<p><span style="font-size: 16px">重复第二步，直到k=1执行简单插入排序。 </span></p>
<p><span style="font-size: 16px"><strong>代码实现：</strong></span></p>
<p><span style="font-size: 16px">首先确定分的组数。</span></p>
<p><span style="font-size: 16px">然后对组中元素进行插入排序。</span></p>
<p><span style="font-size: 16px">然后将length/2，重复1,2步，直到length=0为止。</span></p>
<div class="cnblogs_code">
<pre><span style="color: #008080"> 1</span> <span style="color: #0000ff">public</span> <span style="color: #0000ff">void</span> sheelSort(<span style="color: #0000ff">int</span><span style="color: #000000"> [] a){
</span><span style="color: #008080"> 2</span>         <span style="color: #0000ff">int</span> len=a.length;<span style="color: #008000">//</span><span style="color: #008000">单独把数组长度拿出来，提高效率</span>
<span style="color: #008080"> 3</span>         <span style="color: #0000ff">while</span>(len!=0<span style="color: #000000">){
</span><span style="color: #008080"> 4</span>             len=len/2<span style="color: #000000">;
</span><span style="color: #008080"> 5</span>             <span style="color: #0000ff">for</span>(<span style="color: #0000ff">int</span> i=0;i&lt;len;i++){<span style="color: #008000">//</span><span style="color: #008000">分组</span>
<span style="color: #008080"> 6</span>                 <span style="color: #0000ff">for</span>(<span style="color: #0000ff">int</span> j=i+len;j&lt;a.length;j+=len){<span style="color: #008000">//</span><span style="color: #008000">元素从第二个开始</span>
<span style="color: #008080"> 7</span>                     <span style="color: #0000ff">int</span> k=j-len;<span style="color: #008000">//</span><span style="color: #008000">k为有序序列最后一位的位数</span>
<span style="color: #008080"> 8</span>                     <span style="color: #0000ff">int</span> temp=a[j];<span style="color: #008000">//</span><span style="color: #008000">要插入的元素</span>
<span style="color: #008080"> 9</span>                     <span style="color: #008000">/*</span><span style="color: #008000">for(;k&gt;=0&amp;&amp;temp&lt;a[k];k-=len){
</span><span style="color: #008080">10</span> <span style="color: #008000">                        a[k+len]=a[k];
</span><span style="color: #008080">11</span> <span style="color: #008000">                    }</span><span style="color: #008000">*/</span>
<span style="color: #008080">12</span>                     <span style="color: #0000ff">while</span>(k&gt;=0&amp;&amp;temp&lt;a[k]){<span style="color: #008000">//</span><span style="color: #008000">从后往前遍历</span>
<span style="color: #008080">13</span>                         a[k+len]=<span style="color: #000000">a[k];
</span><span style="color: #008080">14</span>                         k-=len;<span style="color: #008000">//</span><span style="color: #008000">向后移动len位</span>
<span style="color: #008080">15</span> <span style="color: #000000">                    }
</span><span style="color: #008080">16</span>                     a[k+len]=<span style="color: #000000">temp;
</span><span style="color: #008080">17</span> <span style="color: #000000">                }
</span><span style="color: #008080">18</span> <span style="color: #000000">            }
</span><span style="color: #008080">19</span> <span style="color: #000000">        }
</span><span style="color: #008080">20</span>     }</pre>
</div>
<h1>3.简单选择排序</h1>
<p><span style="font-size: 16px">常用于取序列中最大最小的几个数时。</span></p>
<p><span style="font-size: 16px">(如果每次比较都交换，那么就是交换排序；如果每次比较完一个循环再交换，就是简单选择排序。)</span></p>
<p><span style="font-size: 16px">遍历整个序列，将最小的数放在最前面。</span></p>
<p><span style="font-size: 16px">遍历剩下的序列，将最小的数放在最前面。</span></p>
<p><span style="font-size: 16px">重复第二步，直到只剩下一个数。</span></p>
<p><img alt="" src="https://images2015.cnblogs.com/blog/1153367/201704/1153367-20170428152457772-193301923.png"/></p>
<p><span style="font-size: 16px"><strong>代码实现：</strong></span></p>
<p><span style="font-size: 16px">首先确定循环次数，并且记住当前数字和当前位置。</span></p>
<p><span style="font-size: 16px">将当前位置后面所有的数与当前数字进行对比，小数赋值给key，并记住小数的位置。</span></p>
<p><span style="font-size: 16px">比对完成后，将最小的值与第一个数的值交换。</span></p>
<p><span style="font-size: 16px">重复2、3步。</span></p>
<div class="cnblogs_code">
<pre><span style="color: #008080"> 1</span> <span style="color: #0000ff">public</span> <span style="color: #0000ff">void</span> selectSort(<span style="color: #0000ff">int</span><span style="color: #000000">[]a){
</span><span style="color: #008080"> 2</span>         <span style="color: #0000ff">int</span> len=<span style="color: #000000">a.length;
</span><span style="color: #008080"> 3</span>         <span style="color: #0000ff">for</span>(<span style="color: #0000ff">int</span> i=0;i&lt;len;i++){<span style="color: #008000">//</span><span style="color: #008000">循环次数</span>
<span style="color: #008080"> 4</span>             <span style="color: #0000ff">int</span> value=<span style="color: #000000">a[i];
</span><span style="color: #008080"> 5</span>             <span style="color: #0000ff">int</span> position=<span style="color: #000000">i;
</span><span style="color: #008080"> 6</span>             <span style="color: #0000ff">for</span>(<span style="color: #0000ff">int</span> j=i+1;j&lt;len;j++){<span style="color: #008000">//</span><span style="color: #008000">找到最小的值和位置</span>
<span style="color: #008080"> 7</span>                 <span style="color: #0000ff">if</span>(a[j]&lt;<span style="color: #000000">value){
</span><span style="color: #008080"> 8</span>                     value=<span style="color: #000000">a[j];
</span><span style="color: #008080"> 9</span>                     position=<span style="color: #000000">j;
</span><span style="color: #008080">10</span> <span style="color: #000000">                }
</span><span style="color: #008080">11</span> <span style="color: #000000">            }
</span><span style="color: #008080">12</span>             a[position]=a[i];<span style="color: #008000">//</span><span style="color: #008000">进行交换</span>
<span style="color: #008080">13</span>             a[i]=<span style="color: #000000">value;
</span><span style="color: #008080">14</span> <span style="color: #000000">        }
</span><span style="color: #008080">15</span>     }</pre>
</div>
<h1>4.堆排序</h1>
<p><span style="font-size: 16px">对简单选择排序的优化。</span></p>
<p><span style="font-size: 16px">将序列构建成大顶堆。</span></p>
<p><span style="font-size: 16px">将根节点与最后一个节点交换，然后断开最后一个节点。</span></p>
<p><span style="font-size: 16px">重复第一、二步，直到所有节点断开</span>。</p>
<p> <img alt="" src="https://images2015.cnblogs.com/blog/1153367/201704/1153367-20170428153309272-1368116322.png"/></p>
<p>代码如下：</p>
<div class="cnblogs_code">
<pre><span style="color: #008080"> 1</span> <span style="color: #0000ff">public</span>  <span style="color: #0000ff">void</span> heapSort(<span style="color: #0000ff">int</span><span style="color: #000000">[] a){
</span><span style="color: #008080"> 2</span>            <span style="color: #0000ff">int</span> len=<span style="color: #000000">a.length;
</span><span style="color: #008080"> 3</span>            <span style="color: #008000">//</span><span style="color: #008000">循环建堆  </span>
<span style="color: #008080"> 4</span>            <span style="color: #0000ff">for</span>(<span style="color: #0000ff">int</span> i=0;i&lt;len-1;i++<span style="color: #000000">){
</span><span style="color: #008080"> 5</span>                <span style="color: #008000">//</span><span style="color: #008000">建堆  </span>
<span style="color: #008080"> 6</span>                buildMaxHeap(a,len-1-<span style="color: #000000">i);
</span><span style="color: #008080"> 7</span>                <span style="color: #008000">//</span><span style="color: #008000">交换堆顶和最后一个元素  </span>
<span style="color: #008080"> 8</span>                swap(a,0,len-1-<span style="color: #000000">i);
</span><span style="color: #008080"> 9</span> <span style="color: #000000">           }
</span><span style="color: #008080">10</span> <span style="color: #000000">       }
</span><span style="color: #008080">11</span>         <span style="color: #008000">//</span><span style="color: #008000">交换方法</span>
<span style="color: #008080">12</span>        <span style="color: #0000ff">private</span>  <span style="color: #0000ff">void</span> swap(<span style="color: #0000ff">int</span>[] data, <span style="color: #0000ff">int</span> i, <span style="color: #0000ff">int</span><span style="color: #000000"> j) {
</span><span style="color: #008080">13</span>            <span style="color: #0000ff">int</span> tmp=<span style="color: #000000">data[i];
</span><span style="color: #008080">14</span>            data[i]=<span style="color: #000000">data[j];
</span><span style="color: #008080">15</span>            data[j]=<span style="color: #000000">tmp;
</span><span style="color: #008080">16</span> <span style="color: #000000">       }
</span><span style="color: #008080">17</span>        <span style="color: #008000">//</span><span style="color: #008000">对data数组从0到lastIndex建大顶堆  </span>
<span style="color: #008080">18</span>        <span style="color: #0000ff">private</span> <span style="color: #0000ff">void</span> buildMaxHeap(<span style="color: #0000ff">int</span>[] data, <span style="color: #0000ff">int</span><span style="color: #000000"> lastIndex) {
</span><span style="color: #008080">19</span>            <span style="color: #008000">//</span><span style="color: #008000">从lastIndex处节点（最后一个节点）的父节点开始  </span>
<span style="color: #008080">20</span>            <span style="color: #0000ff">for</span>(<span style="color: #0000ff">int</span> i=(lastIndex-1)/2;i&gt;=0;i--<span style="color: #000000">){
</span><span style="color: #008080">21</span>                <span style="color: #008000">//</span><span style="color: #008000">k保存正在判断的节点  </span>
<span style="color: #008080">22</span>                <span style="color: #0000ff">int</span> k=<span style="color: #000000">i;
</span><span style="color: #008080">23</span>                <span style="color: #008000">//</span><span style="color: #008000">如果当前k节点的子节点存在  </span>
<span style="color: #008080">24</span>                <span style="color: #0000ff">while</span>(k*2+1&lt;=<span style="color: #000000">lastIndex){
</span><span style="color: #008080">25</span>                    <span style="color: #008000">//</span><span style="color: #008000">k节点的左子节点的索引  </span>
<span style="color: #008080">26</span>                    <span style="color: #0000ff">int</span> biggerIndex=2*k+1<span style="color: #000000">;
</span><span style="color: #008080">27</span>                    <span style="color: #008000">//</span><span style="color: #008000">如果biggerIndex小于lastIndex，即biggerIndex+1代表的k节点的右子节点存在  </span>
<span style="color: #008080">28</span>                    <span style="color: #0000ff">if</span>(biggerIndex&lt;<span style="color: #000000">lastIndex){
</span><span style="color: #008080">29</span>                        <span style="color: #008000">//</span><span style="color: #008000">若果右子节点的值较大  </span>
<span style="color: #008080">30</span>                        <span style="color: #0000ff">if</span>(data[biggerIndex]&lt;data[biggerIndex+1<span style="color: #000000">]){
</span><span style="color: #008080">31</span>                            <span style="color: #008000">//</span><span style="color: #008000">biggerIndex总是记录较大子节点的索引  </span>
<span style="color: #008080">32</span>                            biggerIndex++<span style="color: #000000">;
</span><span style="color: #008080">33</span> <span style="color: #000000">                       }
</span><span style="color: #008080">34</span> <span style="color: #000000">                   }
</span><span style="color: #008080">35</span>                    <span style="color: #008000">//</span><span style="color: #008000">如果k节点的值小于其较大的子节点的值  </span>
<span style="color: #008080">36</span>                    <span style="color: #0000ff">if</span>(data[k]&lt;<span style="color: #000000">data[biggerIndex]){
</span><span style="color: #008080">37</span>                        <span style="color: #008000">//</span><span style="color: #008000">交换他们  </span>
<span style="color: #008080">38</span> <span style="color: #000000">                       swap(data,k,biggerIndex);
</span><span style="color: #008080">39</span>                        <span style="color: #008000">//</span><span style="color: #008000">将biggerIndex赋予k，开始while循环的下一次循环，重新保证k节点的值大于其左右子节点的值  </span>
<span style="color: #008080">40</span>                        k=<span style="color: #000000">biggerIndex;
</span><span style="color: #008080">41</span>                    }<span style="color: #0000ff">else</span><span style="color: #000000">{
</span><span style="color: #008080">42</span>                        <span style="color: #0000ff">break</span><span style="color: #000000">;
</span><span style="color: #008080">43</span> <span style="color: #000000">                   }
</span><span style="color: #008080">44</span> <span style="color: #000000">               }
</span><span style="color: #008080">45</span> <span style="color: #000000">           }
</span><span style="color: #008080">46</span>        }</pre>
</div>
<h1>5.冒泡排序</h1>
<p><span style="font-size: 16px">很简单，用到的很少，据了解，面试的时候问的比较多！</span></p>
<p>将序列中所有元素两两比较，将最大的放在最后面。</p>
<p>将剩余序列中所有元素两两比较，将最大的放在最后面。</p>
<p>重复第二步，直到只剩下一个数。</p>
<p><img alt="" src="https://images2015.cnblogs.com/blog/1153367/201704/1153367-20170428154208990-180812772.png"/></p>
<p><span style="font-size: 16px">代码实现：</span></p>
<p><span style="font-size: 16px">设置循环次数。</span></p>
<p><span style="font-size: 16px">设置开始比较的位数，和结束的位数。</span></p>
<p><span style="font-size: 16px">两两比较，将最小的放到前面去。</span></p>
<p><span style="font-size: 16px">重复2、3步，直到循环次数完毕。</span></p>
<p> </p>
<div class="cnblogs_code">
<pre><span style="color: #008080"> 1</span>  <span style="color: #0000ff">public</span> <span style="color: #0000ff">void</span> bubbleSort(<span style="color: #0000ff">int</span><span style="color: #000000"> []a){
</span><span style="color: #008080"> 2</span>            <span style="color: #0000ff">int</span> len=<span style="color: #000000">a.length;
</span><span style="color: #008080"> 3</span>            <span style="color: #0000ff">for</span>(<span style="color: #0000ff">int</span> i=0;i&lt;len;i++<span style="color: #000000">){
</span><span style="color: #008080"> 4</span>                <span style="color: #0000ff">for</span>(<span style="color: #0000ff">int</span> j=0;j&lt;len-i-1;j++){<span style="color: #008000">//</span><span style="color: #008000">注意第二重循环的条件</span>
<span style="color: #008080"> 5</span>                    <span style="color: #0000ff">if</span>(a[j]&gt;a[j+1<span style="color: #000000">]){
</span><span style="color: #008080"> 6</span>                        <span style="color: #0000ff">int</span> temp=<span style="color: #000000">a[j];
</span><span style="color: #008080"> 7</span>                        a[j]=a[j+1<span style="color: #000000">];
</span><span style="color: #008080"> 8</span>                        a[j+1]=<span style="color: #000000">temp;
</span><span style="color: #008080"> 9</span> <span style="color: #000000">                   }
</span><span style="color: #008080">10</span> <span style="color: #000000">               }
</span><span style="color: #008080">11</span> <span style="color: #000000">           }
</span><span style="color: #008080">12</span>        }</pre>
</div>
<h1>6.快速排序</h1>
<p><span style="font-size: 16px">要求时间最快时。</span></p>
<p><span style="font-size: 16px">选择第一个数为p，小于p的数放在左边，大于p的数放在右边。</span></p>
<p><span style="font-size: 16px">递归的将p左边和右边的数都按照第一步进行，直到不能递归。</span></p>
<p> <img alt="" src="https://images2015.cnblogs.com/blog/1153367/201704/1153367-20170428154701975-1618466229.png"/></p>
<div class="cnblogs_code">
<pre><span style="color: #008080"> 1</span> <span style="color: #0000ff">public</span> <span style="color: #0000ff">void</span> quickSort(<span style="color: #0000ff">int</span>[]a,<span style="color: #0000ff">int</span> start,<span style="color: #0000ff">int</span><span style="color: #000000"> end){
</span><span style="color: #008080"> 2</span>            <span style="color: #0000ff">if</span>(start&lt;<span style="color: #000000">end){
</span><span style="color: #008080"> 3</span>                <span style="color: #0000ff">int</span> baseNum=a[start];<span style="color: #008000">//</span><span style="color: #008000">选基准值</span>
<span style="color: #008080"> 4</span>                <span style="color: #0000ff">int</span> midNum;<span style="color: #008000">//</span><span style="color: #008000">记录中间值</span>
<span style="color: #008080"> 5</span>                <span style="color: #0000ff">int</span> i=<span style="color: #000000">start;
</span><span style="color: #008080"> 6</span>                <span style="color: #0000ff">int</span> j=<span style="color: #000000">end;
</span><span style="color: #008080"> 7</span>                <span style="color: #0000ff">do</span><span style="color: #000000">{
</span><span style="color: #008080"> 8</span>                    <span style="color: #0000ff">while</span>((a[i]&lt;baseNum)&amp;&amp;i&lt;<span style="color: #000000">end){
</span><span style="color: #008080"> 9</span>                        i++<span style="color: #000000">;
</span><span style="color: #008080">10</span> <span style="color: #000000">                   }
</span><span style="color: #008080">11</span>                    <span style="color: #0000ff">while</span>((a[j]&gt;baseNum)&amp;&amp;j&gt;<span style="color: #000000">start){
</span><span style="color: #008080">12</span>                        j--<span style="color: #000000">;
</span><span style="color: #008080">13</span> <span style="color: #000000">                   }
</span><span style="color: #008080">14</span>                    <span style="color: #0000ff">if</span>(i&lt;=<span style="color: #000000">j){
</span><span style="color: #008080">15</span>                        midNum=<span style="color: #000000">a[i];
</span><span style="color: #008080">16</span>                        a[i]=<span style="color: #000000">a[j];
</span><span style="color: #008080">17</span>                        a[j]=<span style="color: #000000">midNum;
</span><span style="color: #008080">18</span>                        i++<span style="color: #000000">;
</span><span style="color: #008080">19</span>                        j--<span style="color: #000000">;
</span><span style="color: #008080">20</span> <span style="color: #000000">                   }
</span><span style="color: #008080">21</span>                }<span style="color: #0000ff">while</span>(i&lt;=<span style="color: #000000">j);
</span><span style="color: #008080">22</span>                 <span style="color: #0000ff">if</span>(start&lt;<span style="color: #000000">j){
</span><span style="color: #008080">23</span> <span style="color: #000000">                    quickSort(a,start,j);
</span><span style="color: #008080">24</span> <span style="color: #000000">                }       
</span><span style="color: #008080">25</span>                 <span style="color: #0000ff">if</span>(end&gt;<span style="color: #000000">i){
</span><span style="color: #008080">26</span> <span style="color: #000000">                    quickSort(a,i,end);
</span><span style="color: #008080">27</span> <span style="color: #000000">                }
</span><span style="color: #008080">28</span> <span style="color: #000000">           }
</span><span style="color: #008080">29</span>        }</pre>
</div>
<h1>7.归并排序</h1>
<p>速度仅次于快速排序，内存少的时候使用，可以进行并行计算的时候使用。</p>
<p>选择相邻两个数组成一个有序序列。</p>
<p>选择相邻的两个有序序列组成一个有序序列。</p>
<p>重复第二步，直到全部组成一个有序序列。</p>
<p><img alt="" src="https://images2015.cnblogs.com/blog/1153367/201704/1153367-20170428160557053-2123364404.png"/></p>
<div class="cnblogs_code">
<pre><span style="color: #008080"> 1</span> <span style="color: #0000ff">public</span>  <span style="color: #0000ff">void</span> mergeSort(<span style="color: #0000ff">int</span>[] a, <span style="color: #0000ff">int</span> left, <span style="color: #0000ff">int</span><span style="color: #000000"> right) {  
</span><span style="color: #008080"> 2</span>            <span style="color: #0000ff">int</span> t = 1;<span style="color: #008000">//</span><span style="color: #008000"> 每组元素个数  </span>
<span style="color: #008080"> 3</span>            <span style="color: #0000ff">int</span> size = right - left + 1<span style="color: #000000">;  
</span><span style="color: #008080"> 4</span>            <span style="color: #0000ff">while</span> (t &lt;<span style="color: #000000"> size) {  
</span><span style="color: #008080"> 5</span>                <span style="color: #0000ff">int</span> s = t;<span style="color: #008000">//</span><span style="color: #008000"> 本次循环每组元素个数  </span>
<span style="color: #008080"> 6</span>                t = 2 *<span style="color: #000000"> s;  
</span><span style="color: #008080"> 7</span>                <span style="color: #0000ff">int</span> i =<span style="color: #000000"> left;  
</span><span style="color: #008080"> 8</span>                <span style="color: #0000ff">while</span> (i + (t - 1) &lt;<span style="color: #000000"> size) {  
</span><span style="color: #008080"> 9</span>                    merge(a, i, i + (s - 1), i + (t - 1<span style="color: #000000">));  
</span><span style="color: #008080">10</span>                    i +=<span style="color: #000000"> t;  
</span><span style="color: #008080">11</span> <span style="color: #000000">               }  
</span><span style="color: #008080">12</span>                <span style="color: #0000ff">if</span> (i + (s - 1) &lt;<span style="color: #000000"> right)  
</span><span style="color: #008080">13</span>                    merge(a, i, i + (s - 1<span style="color: #000000">), right);  
</span><span style="color: #008080">14</span> <span style="color: #000000">           }  
</span><span style="color: #008080">15</span> <span style="color: #000000">        }  
</span><span style="color: #008080">16</span>        
<span style="color: #008080">17</span>         <span style="color: #0000ff">private</span> <span style="color: #0000ff">static</span> <span style="color: #0000ff">void</span> merge(<span style="color: #0000ff">int</span>[] data, <span style="color: #0000ff">int</span> p, <span style="color: #0000ff">int</span> q, <span style="color: #0000ff">int</span><span style="color: #000000"> r) {  
</span><span style="color: #008080">18</span>            <span style="color: #0000ff">int</span>[] B = <span style="color: #0000ff">new</span> <span style="color: #0000ff">int</span><span style="color: #000000">[data.length];  
</span><span style="color: #008080">19</span>            <span style="color: #0000ff">int</span> s =<span style="color: #000000"> p;  
</span><span style="color: #008080">20</span>            <span style="color: #0000ff">int</span> t = q + 1<span style="color: #000000">;  
</span><span style="color: #008080">21</span>            <span style="color: #0000ff">int</span> k =<span style="color: #000000"> p;  
</span><span style="color: #008080">22</span>            <span style="color: #0000ff">while</span> (s &lt;= q &amp;&amp; t &lt;=<span style="color: #000000"> r) {  
</span><span style="color: #008080">23</span>                <span style="color: #0000ff">if</span> (data[s] &lt;=<span style="color: #000000"> data[t]) {  
</span><span style="color: #008080">24</span>                    B[k] =<span style="color: #000000"> data[s];  
</span><span style="color: #008080">25</span>                    s++<span style="color: #000000">;  
</span><span style="color: #008080">26</span>                } <span style="color: #0000ff">else</span><span style="color: #000000"> {  
</span><span style="color: #008080">27</span>                    B[k] =<span style="color: #000000"> data[t];  
</span><span style="color: #008080">28</span>                    t++<span style="color: #000000">;  
</span><span style="color: #008080">29</span> <span style="color: #000000">               }  
</span><span style="color: #008080">30</span>                k++<span style="color: #000000">;  
</span><span style="color: #008080">31</span> <span style="color: #000000">           }  
</span><span style="color: #008080">32</span>            <span style="color: #0000ff">if</span> (s == q + 1<span style="color: #000000">)  
</span><span style="color: #008080">33</span>                B[k++] = data[t++<span style="color: #000000">];  
</span><span style="color: #008080">34</span>            <span style="color: #0000ff">else</span>  
<span style="color: #008080">35</span>                B[k++] = data[s++<span style="color: #000000">];  
</span><span style="color: #008080">36</span>            <span style="color: #0000ff">for</span> (<span style="color: #0000ff">int</span> i = p; i &lt;= r; i++<span style="color: #000000">)  
</span><span style="color: #008080">37</span>                data[i] =<span style="color: #000000"> B[i];  
</span><span style="color: #008080">38</span>         }</pre>
</div>
<h1>8.基数排序</h1>
<p><span style="font-size: 16px">用于大量数，很长的数进行排序时。</span></p>
<p><span style="font-size: 16px">将所有的数的个位数取出，按照个位数进行排序，构成一个序列。</span></p>
<p><span style="font-size: 16px">将新构成的所有的数的十位数取出，按照十位数进行排序，构成一个序列。</span></p>
<p><span style="font-size: 16px"> 代码实现：</span></p>
<div class="cnblogs_code">
<pre><span style="color: #008080"> 1</span> <span style="color: #0000ff">public</span> <span style="color: #0000ff">void</span> baseSort(<span style="color: #0000ff">int</span><span style="color: #000000">[] a) {
</span><span style="color: #008080"> 2</span>                <span style="color: #008000">//</span><span style="color: #008000">首先确定排序的趟数;    </span>
<span style="color: #008080"> 3</span>                <span style="color: #0000ff">int</span> max = a[0<span style="color: #000000">];
</span><span style="color: #008080"> 4</span>                <span style="color: #0000ff">for</span> (<span style="color: #0000ff">int</span> i = 1; i &lt; a.length; i++<span style="color: #000000">) {
</span><span style="color: #008080"> 5</span>                    <span style="color: #0000ff">if</span> (a[i] &gt;<span style="color: #000000"> max) {
</span><span style="color: #008080"> 6</span>                        max =<span style="color: #000000"> a[i];
</span><span style="color: #008080"> 7</span> <span style="color: #000000">                   }
</span><span style="color: #008080"> 8</span> <span style="color: #000000">               }
</span><span style="color: #008080"> 9</span>                <span style="color: #0000ff">int</span> time = 0<span style="color: #000000">;
</span><span style="color: #008080">10</span>                <span style="color: #008000">//</span><span style="color: #008000">判断位数;    </span>
<span style="color: #008080">11</span>                <span style="color: #0000ff">while</span> (max &gt; 0<span style="color: #000000">) {
</span><span style="color: #008080">12</span>                    max /= 10<span style="color: #000000">;
</span><span style="color: #008080">13</span>                    time++<span style="color: #000000">;
</span><span style="color: #008080">14</span> <span style="color: #000000">               }
</span><span style="color: #008080">15</span>                <span style="color: #008000">//</span><span style="color: #008000">建立10个队列;    </span>
<span style="color: #008080">16</span>                List&lt;ArrayList&lt;Integer&gt;&gt; queue = <span style="color: #0000ff">new</span> ArrayList&lt;ArrayList&lt;Integer&gt;&gt;<span style="color: #000000">();
</span><span style="color: #008080">17</span>                <span style="color: #0000ff">for</span> (<span style="color: #0000ff">int</span> i = 0; i &lt; 10; i++<span style="color: #000000">) {
</span><span style="color: #008080">18</span>                    ArrayList&lt;Integer&gt; queue1 = <span style="color: #0000ff">new</span> ArrayList&lt;Integer&gt;<span style="color: #000000">();
</span><span style="color: #008080">19</span> <span style="color: #000000">                   queue.add(queue1);
</span><span style="color: #008080">20</span> <span style="color: #000000">               }
</span><span style="color: #008080">21</span>                <span style="color: #008000">//</span><span style="color: #008000">进行time次分配和收集;    </span>
<span style="color: #008080">22</span>                <span style="color: #0000ff">for</span> (<span style="color: #0000ff">int</span> i = 0; i &lt; time; i++<span style="color: #000000">) {
</span><span style="color: #008080">23</span>                    <span style="color: #008000">//</span><span style="color: #008000">分配数组元素;    </span>
<span style="color: #008080">24</span>                    <span style="color: #0000ff">for</span> (<span style="color: #0000ff">int</span> j = 0; j &lt; a.length; j++<span style="color: #000000">) {
</span><span style="color: #008080">25</span>                        <span style="color: #008000">//</span><span style="color: #008000">得到数字的第time+1位数;  </span>
<span style="color: #008080">26</span>                        <span style="color: #0000ff">int</span> x = a[j] % (<span style="color: #0000ff">int</span>) Math.pow(10, i + 1) / (<span style="color: #0000ff">int</span>) Math.pow(10<span style="color: #000000">, i);
</span><span style="color: #008080">27</span>                        ArrayList&lt;Integer&gt; queue2 =<span style="color: #000000"> queue.get(x);
</span><span style="color: #008080">28</span> <span style="color: #000000">                       queue2.add(a[j]);
</span><span style="color: #008080">29</span> <span style="color: #000000">                       queue.set(x, queue2);
</span><span style="color: #008080">30</span> <span style="color: #000000">                   }
</span><span style="color: #008080">31</span>                    <span style="color: #0000ff">int</span> count = 0;<span style="color: #008000">//</span><span style="color: #008000">元素计数器;    
</span><span style="color: #008080">32</span>                    <span style="color: #008000">//</span><span style="color: #008000">收集队列元素;    </span>
<span style="color: #008080">33</span>                    <span style="color: #0000ff">for</span> (<span style="color: #0000ff">int</span> k = 0; k &lt; 10; k++<span style="color: #000000">) {
</span><span style="color: #008080">34</span>                        <span style="color: #0000ff">while</span> (queue.get(k).size() &gt; 0<span style="color: #000000">) {
</span><span style="color: #008080">35</span>                            ArrayList&lt;Integer&gt; queue3 =<span style="color: #000000"> queue.get(k);
</span><span style="color: #008080">36</span>                            a[count] = queue3.get(0<span style="color: #000000">);
</span><span style="color: #008080">37</span>                            queue3.remove(0<span style="color: #000000">);
</span><span style="color: #008080">38</span>                            count++<span style="color: #000000">;
</span><span style="color: #008080">39</span> <span style="color: #000000">                       }
</span><span style="color: #008080">40</span> <span style="color: #000000">                   }
</span><span style="color: #008080">41</span> <span style="color: #000000">               }
</span><span style="color: #008080">42</span>         }</pre>
</div>
<p><span style="font-size: 16px"><strong>新建测试类进行测试</strong></span></p>
<div class="cnblogs_code">
<pre><span style="color: #008080"> 1</span> <span style="color: #0000ff">public</span> <span style="color: #0000ff">class</span><span style="color: #000000"> TestSort {
</span><span style="color: #008080"> 2</span>     <span style="color: #0000ff">public</span> <span style="color: #0000ff">static</span> <span style="color: #0000ff">void</span><span style="color: #000000"> main(String[] args) {
</span><span style="color: #008080"> 3</span>         <span style="color: #0000ff">int</span> []a=<span style="color: #0000ff">new</span> <span style="color: #0000ff">int</span>[10<span style="color: #000000">];
</span><span style="color: #008080"> 4</span>         <span style="color: #0000ff">for</span>(<span style="color: #0000ff">int</span> i=1;i&lt;a.length;i++<span style="color: #000000">){
</span><span style="color: #008080"> 5</span>             <span style="color: #008000">//</span><span style="color: #008000">a[i]=(int)(new Random().nextInt(100));</span>
<span style="color: #008080"> 6</span>             a[i]=(<span style="color: #0000ff">int</span>)(Math.random()*100<span style="color: #000000">);
</span><span style="color: #008080"> 7</span> <span style="color: #000000">        }
</span><span style="color: #008080"> 8</span>         System.out.println("排序前的数组为："+<span style="color: #000000">Arrays.toString(a));
</span><span style="color: #008080"> 9</span>         Sort s=<span style="color: #0000ff">new</span><span style="color: #000000"> Sort();
</span><span style="color: #008080">10</span>         <span style="color: #008000">//</span><span style="color: #008000">排序方法测试
</span><span style="color: #008080">11</span>         <span style="color: #008000">//</span><span style="color: #008000">s.insertSort(a);
</span><span style="color: #008080">12</span>         <span style="color: #008000">//</span><span style="color: #008000">s.sheelSort(a);
</span><span style="color: #008080">13</span>         <span style="color: #008000">//</span><span style="color: #008000">s.selectSort(a);
</span><span style="color: #008080">14</span>         <span style="color: #008000">//</span><span style="color: #008000">s.heapSort(a);
</span><span style="color: #008080">15</span>         <span style="color: #008000">//</span><span style="color: #008000">s.bubbleSort(a);
</span><span style="color: #008080">16</span>         <span style="color: #008000">//</span><span style="color: #008000">s.quickSort(a, 1, 9);
</span><span style="color: #008080">17</span>         <span style="color: #008000">//</span><span style="color: #008000">s.mergeSort(a, 3, 7);</span>
<span style="color: #008080">18</span> <span style="color: #000000">        s.baseSort(a);
</span><span style="color: #008080">19</span>         System.out.println("排序后的数组为："+<span style="color: #000000">Arrays.toString(a));
</span><span style="color: #008080">20</span> <span style="color: #000000">    }
</span><span style="color: #008080">21</span> 
<span style="color: #008080">22</span> }</pre>
</div>
<h1><strong>部分结果如下:</strong></h1>
<p><img alt="" src="https://images2015.cnblogs.com/blog/1153367/201704/1153367-20170428161942772-1737598672.png"/></p>
<p><span style="font-size: 16px">如果要进行比较可已加入时间，输出排序时间，从而比较各个排序算法的优缺点，这里不再做介绍。</span></p>
<h1><strong>8.总结：</strong></h1>
<p><span style="font-size: 16px">一、稳定性:</span></p>
<p><span style="font-size: 16px">　   稳定：冒泡排序、插入排序、归并排序和基数排序</span></p>
<p><span style="font-size: 16px">　　不稳定：选择排序、快速排序、希尔排序、堆排序</span></p>
<p><span style="font-size: 16px">二、平均时间复杂度</span></p>
<p><span style="font-size: 16px">　　O(n^2):直接插入排序，简单选择排序，冒泡排序。</span></p>
<p><span style="font-size: 16px">　　在数据规模较小时（9W内），直接插入排序，简单选择排序差不多。当数据较大时，冒泡排序算法的时间代价最高。性能为O(n^2)的算法基本上是相邻元素进行比较，基本上都是稳定的。</span></p>
<p><span style="font-size: 16px">　　O(nlogn):快速排序，归并排序，希尔排序，堆排序。</span></p>
<p><span style="font-size: 16px">　　其中，快排是最好的， 其次是归并和希尔，堆排序在数据量很大时效果明显。</span></p>
<p><span style="font-size: 16px">三、排序算法的选择</span></p>
<p><span style="font-size: 16px">　　1.数据规模较小</span></p>
<p><span style="font-size: 16px">  　　（1）待排序列基本序的情况下，可以选择<strong>直接插入排序</strong>；</span></p>
<p><span style="font-size: 16px">  　　（2）对稳定性不作要求宜用简单选择排序，对稳定性有要求宜用插入或冒泡</span></p>
<p><span style="font-size: 16px">　　2.数据规模不是很大</span></p>
<p><span style="font-size: 16px">　　（1）完全可以用内存空间，序列杂乱无序，对稳定性没有要求，<strong>快速排序</strong>，此时要付出log（N）的额外空间。</span></p>
<p><span style="font-size: 16px">　　（2）序列本身可能有序，对稳定性有要求，空间允许下，宜用归并排序</span></p>
<p><span style="font-size: 16px">　　3.数据规模很大</span></p>
<p><span style="font-size: 16px">   　　（1）对稳定性有求，则可考虑归并排序。</span></p>
<p><span style="font-size: 16px">    　　（2）对稳定性没要求，宜用堆排序</span></p>
<p><span style="font-size: 16px">　　4.序列初始基本有序（正序），宜用直接插入，冒泡</span></p>
<p><span style="font-size: 16px"> 各算法复杂度如下：</span></p>
<p><img alt="" src="https://images2015.cnblogs.com/blog/1153367/201704/1153367-20170428162241834-892470604.png"/></p>
<p> </p>
<div class="clear"></div>
<div id="blog_post_info_block">
<div id="BlogPostCategory"></div>
<div id="EntryTag"></div>
<div id="blog_post_info">
</div>
<div class="clear"></div>
<div id="post_next_prev"></div>
</div>
</div>
</div>

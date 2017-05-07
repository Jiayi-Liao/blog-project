# Hive Lock锁机制
## Hive锁及事务机制概览
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hive作为基于Hdfs的数据存储，跟其他mysql等数据库有着一样的事务机制，但是因为Hive更多的是面向离线数据处理和查询，
所以事务机制相对来说会更简单一些。在Hive中的操作无非就分读和写两种，所以Hive中对应的锁也有两种，分别是互斥锁(Exclusive，简称X)和共享锁(Shared，简称S)。
所谓共享锁(S)和互斥锁(X)，顾名思义就是说，共享锁(S)可以同时由多个命令持有，互斥锁(X)只能由一个命令持有。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这里假设有表A和表B，表A分区为P，表B为非分区表，我们来看看不同操作下所产生的锁是怎样的：
<table>
  <thead>
    <tr>
      <th>Hive命令</th>
      <th>锁</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>select * from A where partition='P'</td>
      <td>A表分区P(S)，A表(S)</td>
    </tr>
    <tr>
      <td>select * from B</td>
      <td>B表(S)</td>
    </tr>
    <tr>
      <td>insert overwrite table A(partition='P') select * from B</td>
      <td>A表分区P(S)，A表(X)，B表(S)</td>
    </tr>
  </tbody>
</table>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由上表可以总结出以下结论:      

* 查询对应共享锁(S)，写入对应互斥锁(X)
* 当对分区进行查询，表和分区都会产生共享锁(S)，当对分区进行写入，只有分区会产生互斥锁(X)，表产生共享锁(S)

## Hive锁原理探究
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;之前提到共享锁(S)可以同时由多个命令持有，互斥锁(X)只能由一个命令持有，这个很好理解，
因为多个查询同时进行不存在问题，但是多个写入操作进行的话，就会产生不一致问题。现在我们来看看在Hive内部锁获取具体是怎样去实现的。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们可以看到在zookeeper根目录下有一个跟hive有关的目录，

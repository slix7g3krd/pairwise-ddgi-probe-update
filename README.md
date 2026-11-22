# pairwise-ddgi-probe-update

## 领域

游戏、图形与多媒体

## 主题

DDGI 探针更新

## 说明

更新队列、级联边界混合与失效标记。

初始状态下 `render/ddgi_probe_update.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。

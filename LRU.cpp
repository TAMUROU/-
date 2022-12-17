class LRUCache {
private:
  list<pair<int, int>> cache;
  unordered_map<int, list<pair<int, int>>::iterator> MAP;//参考题解，使用迭代器，减少了代码量 
  int Size;

public:
  LRUCache(int capacity) : Size(capacity) {}


int get(int key) {
    if(MAP.find(key) == MAP.end())
		return -1;//不存在，返回-1 
    else
    {
        cache.splice(cache.begin(), cache, MAP[key]);//更新缓存列表 ，将被查询对象提前 
        return MAP[key]->second;
    }
}

void put(int key, int value) {
    if(get(key) != -1)
		MAP[key]->second = value;//存在，赋值 
    else    
    {   //不存在，新建结点 
        if(cache.size() == Size)//若已满，删除最前结点 
        {
            int del = cache.back().first;
            cache.pop_back();
            MAP.erase(del);
        }
        cache.emplace_front(key, value);//添加新节点 
        MAP[key] = cache.begin();
    }
}
};


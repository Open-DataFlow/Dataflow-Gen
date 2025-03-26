import importlib.util
import types
import os

class LazyLoader(types.ModuleType):

    def __init__(self, name, path, import_structure):
        """
        初始化 LazyLoader 模块。

        :param name: 模块名称
        :param import_structure: 定义类名到文件路径的映射字典
        """
        super().__init__(name)
        self._import_structure = import_structure
        self._loaded_classes = {}
        self.__path__ = [path]

    def _load_class_from_file(self, file_path, class_name):
        """
        从指定文件中加载类。

        :param file_path: 脚本文件的路径
        :param class_name: 类的名字
        :return: 类对象
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} does not exist")
        
        # 动态加载模块
        spec = importlib.util.spec_from_file_location(class_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # 提取类
        if not hasattr(module, class_name):
            raise AttributeError(f"Class {class_name} not found in {file_path}")
        return getattr(module, class_name)

    def __getattr__(self, item):
        """
        动态加载类。

        :param item: 类名
        :return: 动态加载的类对象
        """
        if item in self._loaded_classes:
            return self._loaded_classes[item]
        # 从映射结构中获取文件路径和类名
        if item in self._import_structure:
            file_path, class_name = self._import_structure[item]
            cls = self._load_class_from_file(file_path, class_name)
            self._loaded_classes[item] = cls
            return cls
        raise AttributeError(f"Module {self.__name__} has no attribute {item}")

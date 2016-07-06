'''
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
'''
from abc import abstractmethod

__author__ = 'Marko A. Rodriguez (http://markorodriguez.com)'

TO_JAVA_MAP = {"_global": "global", "_as": "as", "_in": "in", "_and": "and",
               "_or": "or", "_is": "is", "_not": "not", "_from": "from",
               "Cardinality": "VertexProperty.Cardinality", "Barrier": "SackFunctions.Barrier"}


class Translator(object):
    def __init__(self, traversal_source, anonymous_traversal, target_language):
        self.traversal_source = traversal_source
        self.anonymous_traversal = anonymous_traversal
        self.target_language = target_language

    @abstractmethod
    def translate(self, bytecode):
        return

    @abstractmethod
    def __repr__(self):
        return "translator[" + self.traversal_source + ":" + self.target_language + "]"


class SymbolHelper(object):
    @staticmethod
    def toJava(symbol):
        if (symbol in TO_JAVA_MAP):
            return TO_JAVA_MAP[symbol]
        else:
            return symbol

    @staticmethod
    def mapEnum(enum):
        if (enum in enumMap):
            return enumMap[enum]
        else:
            return enum

# Copyright (c) 2022 spdx contributors
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import List


class Logger:
    messages: List[str]

    def __init__(self):
        self.messages = []

    def append(self, message: str):
        self.messages.append(message)

    def extend(self, messages_to_append: List[str]):
        self.messages.extend(messages_to_append)

    def has_messages(self):
        return bool(self.messages)

    def get_messages(self):
        return list(self.messages)

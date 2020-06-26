# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from mlagents_envs.communicator_objects.agent_action_pb2 import (
    AgentActionProto as mlagents_envs___communicator_objects___agent_action_pb2___AgentActionProto,
)

from mlagents_envs.communicator_objects.agent_info_pb2 import (
    AgentInfoProto as mlagents_envs___communicator_objects___agent_info_pb2___AgentInfoProto,
)

from typing import (
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class AgentInfoActionPairProto(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def agent_info(self) -> mlagents_envs___communicator_objects___agent_info_pb2___AgentInfoProto: ...

    @property
    def action_info(self) -> mlagents_envs___communicator_objects___agent_action_pb2___AgentActionProto: ...

    def __init__(self,
        *,
        agent_info : typing___Optional[mlagents_envs___communicator_objects___agent_info_pb2___AgentInfoProto] = None,
        action_info : typing___Optional[mlagents_envs___communicator_objects___agent_action_pb2___AgentActionProto] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"action_info",b"action_info",u"agent_info",b"agent_info"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"action_info",b"action_info",u"agent_info",b"agent_info"]) -> None: ...
type___AgentInfoActionPairProto = AgentInfoActionPairProto

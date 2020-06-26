# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from mlagents_envs.communicator_objects.unity_rl_initialization_output_pb2 import (
    UnityRLInitializationOutputProto as mlagents_envs___communicator_objects___unity_rl_initialization_output_pb2___UnityRLInitializationOutputProto,
)

from mlagents_envs.communicator_objects.unity_rl_output_pb2 import (
    UnityRLOutputProto as mlagents_envs___communicator_objects___unity_rl_output_pb2___UnityRLOutputProto,
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

class UnityOutputProto(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def rl_output(self) -> mlagents_envs___communicator_objects___unity_rl_output_pb2___UnityRLOutputProto: ...

    @property
    def rl_initialization_output(self) -> mlagents_envs___communicator_objects___unity_rl_initialization_output_pb2___UnityRLInitializationOutputProto: ...

    def __init__(self,
        *,
        rl_output : typing___Optional[mlagents_envs___communicator_objects___unity_rl_output_pb2___UnityRLOutputProto] = None,
        rl_initialization_output : typing___Optional[mlagents_envs___communicator_objects___unity_rl_initialization_output_pb2___UnityRLInitializationOutputProto] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"rl_initialization_output",b"rl_initialization_output",u"rl_output",b"rl_output"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"rl_initialization_output",b"rl_initialization_output",u"rl_output",b"rl_output"]) -> None: ...
type___UnityOutputProto = UnityOutputProto

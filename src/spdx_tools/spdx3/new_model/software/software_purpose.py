# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_python_model_from_spec.py
# Do not manually edit!
# flake8: noqa

from enum import Enum, auto

from beartype.typing import Optional


class SoftwarePurpose(Enum):
    """
    This field provides information about the primary purpose of an Element. Software Purpose is intrinsic to how the
    Element is being used rather than the content of the Element. This field is a reasonable estimate of the most
    likely usage of the Element from the producer and consumer perspective from which both parties can draw conclusions
    about the context in which the Element exists.
    """

    APPLICATION = auto()
    """
    the Element is a software application
    """
    ARCHIVE = auto()
    """
    the Element is an archived collection of one or more files (.tar, .zip, etc)
    """
    BOM = auto()
    """
    Element is a bill of materials
    """
    CONFIGURATION = auto()
    """
    Element is configuration data
    """
    CONTAINER = auto()
    """
    the Element is a container image which can be used by a container runtime application
    """
    DATA = auto()
    """
    Element is data
    """
    DEVICE = auto()
    """
    the Element refers to a chipset, processor, or electronic board
    """
    DOCUMENTATION = auto()
    """
    Element is documentation
    """
    EVIDENCE = auto()
    """
    the Element is the evidence that a specification or requirement has been fulfilled
    """
    EXECUTABLE = auto()
    """
    Element is an Artifact that can be run on a computer
    """
    FILE = auto()
    """
    the Element is a single file which can be independently distributed (configuration file, statically linked binary,
    Kubernetes deployment, etc)
    """
    FIRMWARE = auto()
    """
    the Element provides low level control over a device's hardware
    """
    FRAMEWORK = auto()
    """
    the Element is a software framework
    """
    INSTALL = auto()
    """
    the Element is used to install software on disk
    """
    LIBRARY = auto()
    """
    the Element is a software library
    """
    MANIFEST = auto()
    """
    the Element is a software manifest
    """
    MODEL = auto()
    """
    the Element is a machine learning or artificial intelligence model
    """
    MODULE = auto()
    """
    the Element is a module of a piece of software
    """
    OPERATING_SYSTEM = auto()
    """
    the Element is an operating system
    """
    OTHER = auto()
    """
    the Element doesn't fit into any of the other categories
    """
    PATCH = auto()
    """
    Element contains a set of changes to update, fix, or improve another Element
    """
    REQUIREMENT = auto()
    """
    the Element provides a requirement needed as input for another Element
    """
    SOURCE = auto()
    """
    the Element is a single or a collection of source files
    """
    SPECIFICATION = auto()
    """
    the Element is a plan, guideline or strategy how to create, perform or analyse an application
    """
    TEST = auto()
    """
    The Element is a test used to verify functionality on an software element
    """

    def __str__(self) -> str:
        if self == SoftwarePurpose.APPLICATION:
            return "application"
        if self == SoftwarePurpose.ARCHIVE:
            return "archive"
        if self == SoftwarePurpose.BOM:
            return "bom"
        if self == SoftwarePurpose.CONFIGURATION:
            return "configuration"
        if self == SoftwarePurpose.CONTAINER:
            return "container"
        if self == SoftwarePurpose.DATA:
            return "data"
        if self == SoftwarePurpose.DEVICE:
            return "device"
        if self == SoftwarePurpose.DOCUMENTATION:
            return "documentation"
        if self == SoftwarePurpose.EVIDENCE:
            return "evidence"
        if self == SoftwarePurpose.EXECUTABLE:
            return "executable"
        if self == SoftwarePurpose.FILE:
            return "file"
        if self == SoftwarePurpose.FIRMWARE:
            return "firmware"
        if self == SoftwarePurpose.FRAMEWORK:
            return "framework"
        if self == SoftwarePurpose.INSTALL:
            return "install"
        if self == SoftwarePurpose.LIBRARY:
            return "library"
        if self == SoftwarePurpose.MANIFEST:
            return "manifest"
        if self == SoftwarePurpose.MODEL:
            return "model"
        if self == SoftwarePurpose.MODULE:
            return "module"
        if self == SoftwarePurpose.OPERATING_SYSTEM:
            return "operatingSystem"
        if self == SoftwarePurpose.OTHER:
            return "other"
        if self == SoftwarePurpose.PATCH:
            return "patch"
        if self == SoftwarePurpose.REQUIREMENT:
            return "requirement"
        if self == SoftwarePurpose.SOURCE:
            return "source"
        if self == SoftwarePurpose.SPECIFICATION:
            return "specification"
        if self == SoftwarePurpose.TEST:
            return "test"
        return "unknown"

    @staticmethod
    def from_str(value: str) -> Optional["SoftwarePurpose"]:
        if value == "application":
            return SoftwarePurpose.APPLICATION
        if value == "archive":
            return SoftwarePurpose.ARCHIVE
        if value == "bom":
            return SoftwarePurpose.BOM
        if value == "configuration":
            return SoftwarePurpose.CONFIGURATION
        if value == "container":
            return SoftwarePurpose.CONTAINER
        if value == "data":
            return SoftwarePurpose.DATA
        if value == "device":
            return SoftwarePurpose.DEVICE
        if value == "documentation":
            return SoftwarePurpose.DOCUMENTATION
        if value == "evidence":
            return SoftwarePurpose.EVIDENCE
        if value == "executable":
            return SoftwarePurpose.EXECUTABLE
        if value == "file":
            return SoftwarePurpose.FILE
        if value == "firmware":
            return SoftwarePurpose.FIRMWARE
        if value == "framework":
            return SoftwarePurpose.FRAMEWORK
        if value == "install":
            return SoftwarePurpose.INSTALL
        if value == "library":
            return SoftwarePurpose.LIBRARY
        if value == "manifest":
            return SoftwarePurpose.MANIFEST
        if value == "model":
            return SoftwarePurpose.MODEL
        if value == "module":
            return SoftwarePurpose.MODULE
        if value == "operatingSystem":
            return SoftwarePurpose.OPERATING_SYSTEM
        if value == "other":
            return SoftwarePurpose.OTHER
        if value == "patch":
            return SoftwarePurpose.PATCH
        if value == "requirement":
            return SoftwarePurpose.REQUIREMENT
        if value == "source":
            return SoftwarePurpose.SOURCE
        if value == "specification":
            return SoftwarePurpose.SPECIFICATION
        if value == "test":
            return SoftwarePurpose.TEST
        return None

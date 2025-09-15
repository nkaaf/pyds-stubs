# ruff: noqa: PYI021
# ruff: noqa: N801
# ruff: noqa: N802
# ruff: noqa: N803
# ruff: noqa: N815
# ruff: noqa: D205
# ruff: noqa: D415
# ruff: noqa: D418
# ruff: noqa: D419
# ruff: noqa: A002
# ruff: noqa: ANN002
# ruff: noqa: ANN003
# ruff: noqa: ANN205
# ruff: noqa: ANN401
# ruff: noqa: ERA001
# ruff: noqa: UP045 - This check is for Python >= 3.10

"""pybind11 bindings for gstnvdsmeta."""

import typing

import numpy
from gi.repository import GLib, Gst
from numpy.typing import NDArray

from pyds.typing import GList, capsule

__all__: list[str] = [
    "BOTH_HEAD",
    "END_HEAD",
    "FLOAT",
    "HALF",
    "INSIDE_AISLE_360D",
    "INT8",
    "INT32",
    "MODE_CPU",
    "MODE_GPU",
    "MODE_HW",
    "NVBUF_COLOR_FORMAT_ABGR",
    "NVBUF_COLOR_FORMAT_ARGB",
    "NVBUF_COLOR_FORMAT_BGR",
    "NVBUF_COLOR_FORMAT_BGRA",
    "NVBUF_COLOR_FORMAT_GRAY8",
    "NVBUF_COLOR_FORMAT_INVALID",
    "NVBUF_COLOR_FORMAT_LAST",
    "NVBUF_COLOR_FORMAT_NV12",
    "NVBUF_COLOR_FORMAT_NV12_10LE",
    "NVBUF_COLOR_FORMAT_NV12_10LE_709",
    "NVBUF_COLOR_FORMAT_NV12_10LE_709_ER",
    "NVBUF_COLOR_FORMAT_NV12_10LE_2020",
    "NVBUF_COLOR_FORMAT_NV12_10LE_ER",
    "NVBUF_COLOR_FORMAT_NV12_12LE",
    "NVBUF_COLOR_FORMAT_NV12_709",
    "NVBUF_COLOR_FORMAT_NV12_709_ER",
    "NVBUF_COLOR_FORMAT_NV12_2020",
    "NVBUF_COLOR_FORMAT_NV12_ER",
    "NVBUF_COLOR_FORMAT_NV21",
    "NVBUF_COLOR_FORMAT_NV21_ER",
    "NVBUF_COLOR_FORMAT_RGB",
    "NVBUF_COLOR_FORMAT_RGBA",
    "NVBUF_COLOR_FORMAT_SIGNED_R16G16",
    "NVBUF_COLOR_FORMAT_UYVY",
    "NVBUF_COLOR_FORMAT_UYVY_ER",
    "NVBUF_COLOR_FORMAT_VYUY",
    "NVBUF_COLOR_FORMAT_VYUY_ER",
    "NVBUF_COLOR_FORMAT_YUV420",
    "NVBUF_COLOR_FORMAT_YUV420_709",
    "NVBUF_COLOR_FORMAT_YUV420_709_ER",
    "NVBUF_COLOR_FORMAT_YUV420_2020",
    "NVBUF_COLOR_FORMAT_YUV420_ER",
    "NVBUF_COLOR_FORMAT_YUV444",
    "NVBUF_COLOR_FORMAT_YUYV",
    "NVBUF_COLOR_FORMAT_YUYV_ER",
    "NVBUF_COLOR_FORMAT_YVU420",
    "NVBUF_COLOR_FORMAT_YVU420_ER",
    "NVBUF_COLOR_FORMAT_YVYU",
    "NVBUF_COLOR_FORMAT_YVYU_ER",
    "NVBUF_LAYOUT_BLOCK_LINEAR",
    "NVBUF_LAYOUT_PITCH",
    "NVBUF_MAP_READ",
    "NVBUF_MAP_READ_WRITE",
    "NVBUF_MAP_WRITE",
    "NVBUF_MEM_CUDA_DEVICE",
    "NVBUF_MEM_CUDA_PINNED",
    "NVBUF_MEM_CUDA_UNIFIED",
    "NVBUF_MEM_DEFAULT",
    "NVBUF_MEM_HANDLE",
    "NVBUF_MEM_SURFACE_ARRAY",
    "NVBUF_MEM_SYSTEM",
    "NVDSINFER_SEGMENTATION_META",
    "NVDSINFER_TENSOR_OUTPUT_META",
    "NVDS_AUDIO_BATCH_META",
    "NVDS_AUDIO_FRAME_META",
    "NVDS_BATCH_GST_META",
    "NVDS_BATCH_META",
    "NVDS_CLASSIFIER_META",
    "NVDS_CROP_IMAGE_META",
    "NVDS_DECODER_GST_META",
    "NVDS_DEWARPER_GST_META",
    "NVDS_DISPLAY_META",
    "NVDS_EVENT_CUSTOM",
    "NVDS_EVENT_EMPTY",
    "NVDS_EVENT_ENTRY",
    "NVDS_EVENT_EXIT",
    "NVDS_EVENT_FORCE32",
    "NVDS_EVENT_MOVING",
    "NVDS_EVENT_MSG_META",
    "NVDS_EVENT_PARKED",
    "NVDS_EVENT_RESERVED",
    "NVDS_EVENT_RESET",
    "NVDS_EVENT_STOPPED",
    "NVDS_FORCE32_META",
    "NVDS_FRAME_META",
    "NVDS_GST_CUSTOM_META",
    "NVDS_GST_INVALID_META",
    "NVDS_GST_META_FORCE32",
    "NVDS_INVALID_META",
    "NVDS_LABEL_INFO_META",
    "NVDS_LATENCY_MEASUREMENT_META",
    "NVDS_OBEJCT_TYPE_FORCE32",
    "NVDS_OBJECT_TYPE_BAG",
    "NVDS_OBJECT_TYPE_BICYCLE",
    "NVDS_OBJECT_TYPE_CUSTOM",
    "NVDS_OBJECT_TYPE_FACE",
    "NVDS_OBJECT_TYPE_FACE_EXT",
    "NVDS_OBJECT_TYPE_PERSON",
    "NVDS_OBJECT_TYPE_PERSON_EXT",
    "NVDS_OBJECT_TYPE_RESERVED",
    "NVDS_OBJECT_TYPE_ROADSIGN",
    "NVDS_OBJECT_TYPE_UNKNOWN",
    "NVDS_OBJECT_TYPE_VEHICLE",
    "NVDS_OBJECT_TYPE_VEHICLE_EXT",
    "NVDS_OBJ_META",
    "NVDS_OPTICAL_FLOW_META",
    "NVDS_PAYLOAD_CUSTOM",
    "NVDS_PAYLOAD_DEEPSTREAM",
    "NVDS_PAYLOAD_DEEPSTREAM_MINIMAL",
    "NVDS_PAYLOAD_FORCE32",
    "NVDS_PAYLOAD_META",
    "NVDS_PAYLOAD_RESERVED",
    "NVDS_RESERVED_GST_META",
    "NVDS_RESERVED_META",
    "NVDS_START_USER_META",
    "NVDS_TRACKER_PAST_FRAME_META",
    "NVDS_USER_META",
    "ROI_ENTRY_360D",
    "ROI_EXIT_360D",
    "ROI_STATUS_360D",
    "START_HEAD",
    "GstNvDsMetaType",
    "NVBUF_COLOR_FORMAT_BGRx",
    "NVBUF_COLOR_FORMAT_RGBx",
    "NVBUF_COLOR_FORMAT_xBGR",
    "NVBUF_COLOR_FORMAT_xRGB",
    "NvBbox_Coords",
    "NvBufSurface",
    "NvBufSurfaceColorFormat",
    "NvBufSurfaceCopy",
    "NvBufSurfaceCreate",
    "NvBufSurfaceCreateParams",
    "NvBufSurfaceDestroy",
    "NvBufSurfaceFromFd",
    "NvBufSurfaceLayout",
    "NvBufSurfaceMap",
    "NvBufSurfaceMapEglImage",
    "NvBufSurfaceMappedAddr",
    "NvBufSurfaceMemMapFlags",
    "NvBufSurfaceMemSet",
    "NvBufSurfaceMemType",
    "NvBufSurfaceParams",
    "NvBufSurfacePlaneParams",
    "NvBufSurfaceSyncForCpu",
    "NvBufSurfaceSyncForDevice",
    "NvBufSurfaceUnMap",
    "NvDsAnalyticsFrameMeta",
    "NvDsAnalyticsObjInfo",
    "NvDsBaseMeta",
    "NvDsBatchMeta",
    "NvDsClassifierMeta",
    "NvDsComp_BboxInfo",
    "NvDsCoordinate",
    "NvDsDisplayMeta",
    "NvDsEvent",
    "NvDsEventMsgMeta",
    "NvDsEventType",
    "NvDsFaceObject",
    "NvDsFaceObjectWithExt",
    "NvDsFrameMeta",
    "NvDsGeoLocation",
    "NvDsInferAttribute",
    "NvDsInferDataType",
    "NvDsInferDims",
    "NvDsInferDimsCHW",
    "NvDsInferLayerInfo",
    "NvDsInferNetworkInfo",
    "NvDsInferObjectDetectionInfo",
    "NvDsInferSegmentationMeta",
    "NvDsInferTensorMeta",
    "NvDsLabelInfo",
    "NvDsMeta",
    "NvDsMetaPool",
    "NvDsMetaType",
    "NvDsObjectMeta",
    "NvDsObjectSignature",
    "NvDsObjectType",
    "NvDsOpticalFlowMeta",
    "NvDsPastFrameObj",
    "NvDsPastFrameObjBatch",
    "NvDsPastFrameObjList",
    "NvDsPastFrameObjStream",
    "NvDsPayload",
    "NvDsPayloadType",
    "NvDsPersonObject",
    "NvDsPersonObjectExt",
    "NvDsRect",
    "NvDsUserMeta",
    "NvDsVehicleObject",
    "NvDsVehicleObjectExt",
    "NvOFFlowVector",
    "NvOSD_ArrowParams",
    "NvOSD_Arrow_Head_Direction",
    "NvOSD_CircleParams",
    "NvOSD_ColorParams",
    "NvOSD_Color_info",
    "NvOSD_FontParams",
    "NvOSD_FrameArrowParams",
    "NvOSD_FrameCircleParams",
    "NvOSD_FrameLineParams",
    "NvOSD_FrameRectParams",
    "NvOSD_FrameTextParams",
    "NvOSD_LineParams",
    "NvOSD_Mode",
    "NvOSD_RectParams",
    "NvOSD_TextParams",
    "RectDim",
    "alloc_buffer",
    "alloc_char_buffer",
    "alloc_nvds_event",
    "alloc_nvds_event_msg_meta",
    "alloc_nvds_face_object",
    "alloc_nvds_payload",
    "alloc_nvds_person_object",
    "alloc_nvds_vehicle_object",
    "free_buffer",
    "free_gbuffer",
    "generate_ts_rfc3339",
    "get_detections",
    "get_nvds_LayerInfo",
    "get_nvds_buf_surface",
    "get_optical_flow_vectors",
    "get_ptr",
    "get_segmentation_masks",
    "get_string",
    "glist_get_nvds_Surface_Params",
    "glist_get_nvds_batch_meta",
    "glist_get_nvds_classifier_meta",
    "glist_get_nvds_display_meta",
    "glist_get_nvds_event_msg_meta",
    "glist_get_nvds_frame_meta",
    "glist_get_nvds_label_info",
    "glist_get_nvds_object_meta",
    "glist_get_nvds_person_object",
    "glist_get_nvds_tensor_meta",
    "glist_get_nvds_user_meta",
    "glist_get_nvds_vehicle_object",
    "gst_buffer_add_nvds_meta",
    "gst_buffer_get_nvds_batch_meta",
    "memdup",
    "nvds_acquire_classifier_meta_from_pool",
    "nvds_acquire_display_meta_from_pool",
    "nvds_acquire_frame_meta_from_pool",
    "nvds_acquire_label_info_meta_from_pool",
    "nvds_acquire_meta_lock",
    "nvds_acquire_obj_meta_from_pool",
    "nvds_acquire_user_meta_from_pool",
    "nvds_add_classifier_meta_to_object",
    "nvds_add_display_meta_to_frame",
    "nvds_add_frame_meta_to_batch",
    "nvds_add_label_info_meta_to_classifier",
    "nvds_add_obj_meta_to_frame",
    "nvds_add_user_meta_to_batch",
    "nvds_add_user_meta_to_frame",
    "nvds_add_user_meta_to_obj",
    "nvds_batch_meta_copy_func",
    "nvds_batch_meta_release_func",
    "nvds_clear_batch_user_meta_list",
    "nvds_clear_display_meta_list",
    "nvds_clear_frame_meta_list",
    "nvds_clear_frame_user_meta_list",
    "nvds_clear_meta_list",
    "nvds_clear_obj_meta_list",
    "nvds_clear_obj_user_meta_list",
    "nvds_copy_batch_user_meta_list",
    "nvds_copy_display_meta_list",
    "nvds_copy_frame_meta_list",
    "nvds_copy_frame_user_meta_list",
    "nvds_copy_obj_meta_list",
    "nvds_create_batch_meta",
    "nvds_destroy_batch_meta",
    "nvds_get_current_metadata_info",
    "nvds_get_nth_frame_meta",
    "nvds_get_user_meta_type",
    "nvds_release_meta_lock",
    "nvds_remove_classifier_meta_from_obj",
    "nvds_remove_display_meta_from_frame",
    "nvds_remove_frame_meta_from_batch",
    "nvds_remove_label_info_meta_from_classifier",
    "nvds_remove_obj_meta_from_frame",
    "nvds_remove_user_meta_from_batch",
    "nvds_remove_user_meta_from_frame",
    "nvds_remove_user_meta_from_object",
    "register_user_copyfunc",
    "register_user_releasefunc",
    "set_user_copyfunc",
    "set_user_releasefunc",
    "strdup",
    "strdup2str",
    "unset_callback_funcs",
    "user_copyfunc",
    "user_releasefunc",
]


class GstNvDsMetaType:
    """Members:

    NVDS_GST_INVALID_META

    NVDS_BATCH_GST_META

    NVDS_DECODER_GST_META

    NVDS_DEWARPER_GST_META

    NVDS_RESERVED_GST_META

    NVDS_GST_META_FORCE32
    """

    NVDS_BATCH_GST_META: typing.ClassVar[
        GstNvDsMetaType
    ]  # value = GstNvDsMetaType.NVDS_BATCH_GST_META
    NVDS_DECODER_GST_META: typing.ClassVar[
        GstNvDsMetaType
    ]  # value = GstNvDsMetaType.NVDS_DECODER_GST_META
    NVDS_DEWARPER_GST_META: typing.ClassVar[
        GstNvDsMetaType
    ]  # value = GstNvDsMetaType.NVDS_DEWARPER_GST_META
    NVDS_GST_INVALID_META: typing.ClassVar[
        GstNvDsMetaType
    ]  # value = GstNvDsMetaType.NVDS_GST_INVALID_META
    NVDS_GST_META_FORCE32: typing.ClassVar[
        GstNvDsMetaType
    ]  # value = GstNvDsMetaType.NVDS_GST_META_FORCE32
    NVDS_RESERVED_GST_META: typing.ClassVar[
        GstNvDsMetaType
    ]  # value = GstNvDsMetaType.NVDS_RESERVED_GST_META
    __members__: typing.ClassVar[
        dict[str, GstNvDsMetaType]
    ]  # value = {'NVDS_GST_INVALID_META': GstNvDsMetaType.NVDS_GST_INVALID_META,

    # 'NVDS_BATCH_GST_META': GstNvDsMetaType.NVDS_BATCH_GST_META,
    # 'NVDS_DECODER_GST_META': GstNvDsMetaType.NVDS_DECODER_GST_META,
    # 'NVDS_DEWARPER_GST_META': GstNvDsMetaType.NVDS_DEWARPER_GST_META,
    # 'NVDS_RESERVED_GST_META': GstNvDsMetaType.NVDS_RESERVED_GST_META,
    # 'NVDS_GST_META_FORCE32': GstNvDsMetaType.NVDS_GST_META_FORCE32}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str"""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.GstNvDsMetaType, arg0: int) -> None"""

    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...


class NvBbox_Coords:
    """Holds unclipped bounding box coordinates of the object."""

    def __init__(self) -> None: ...
    @property
    def height(self) -> float:
        """Holds the box's height in pixels."""

    @height.setter
    def height(self, arg0: float) -> None: ...
    @property
    def left(self) -> float:
        """Holds the box's left coordinate in pixels."""

    @left.setter
    def left(self, arg0: float) -> None: ...
    @property
    def top(self) -> float:
        """Holds the box's top coordinate in pixels."""

    @top.setter
    def top(self, arg0: float) -> None: ...
    @property
    def width(self) -> float:
        """Holds the box's width in pixels."""

    @width.setter
    def width(self, arg0: float) -> None: ...


class NvBufSurface:
    def __init__(self) -> None: ...
    @property
    def batchSize(self) -> int:
        """BatchSize"""

    @property
    def gpuId(self) -> int:
        """GpuId"""

    @property
    def isContiguous(self) -> bool:
        """IsContiguous"""

    @property
    def memType(self) -> NvBufSurfaceMemType:
        """MemType"""

    @property
    def numFilled(self) -> int:
        """NumFilled"""

    @property
    def surfaceList(self) -> NvBufSurfaceParams:
        """SurfaceList"""


class NvBufSurfaceColorFormat:
    """Members:

    NVBUF_COLOR_FORMAT_INVALID : NVBUF_COLOR_FORMAT_INVALID

    NVBUF_COLOR_FORMAT_GRAY8 : 8 bit GRAY scale - single plane

    NVBUF_COLOR_FORMAT_YUV420 : BT.601 colorspace - YUV420 multi-planar.

    NVBUF_COLOR_FORMAT_YVU420 : BT.601 colorspace - YUV420 multi-planar.

    NVBUF_COLOR_FORMAT_YUV420_ER : BT.601 colorspace - YUV420 ER multi-planar.

    NVBUF_COLOR_FORMAT_YVU420_ER : BT.601 colorspace - YVU420 ER multi-planar.

    NVBUF_COLOR_FORMAT_NV12 : BT.601 colorspace - Y/CbCr 4:2:0 multi-planar.

    NVBUF_COLOR_FORMAT_NV12_ER : BT.601 colorspace - Y/CbCr ER 4:2:0 multi-planar.

    NVBUF_COLOR_FORMAT_NV21 : BT.601 colorspace - Y/CbCr 4:2:0 multi-planar.

    NVBUF_COLOR_FORMAT_NV21_ER : BT.601 colorspace - Y/CbCr ER 4:2:0 multi-planar.

    NVBUF_COLOR_FORMAT_UYVY : BT.601 colorspace - YUV 4:2:2 planar.

    NVBUF_COLOR_FORMAT_UYVY_ER : BT.601 colorspace - YUV ER 4:2:2 planar.

    NVBUF_COLOR_FORMAT_VYUY : BT.601 colorspace - YUV 4:2:2 planar.

    NVBUF_COLOR_FORMAT_VYUY_ER : BT.601 colorspace - YUV ER 4:2:2 planar.

    NVBUF_COLOR_FORMAT_YUYV : BT.601 colorspace - YUV 4:2:2 planar.

    NVBUF_COLOR_FORMAT_YUYV_ER : BT.601 colorspace - YUV ER 4:2:2 planar.

    NVBUF_COLOR_FORMAT_YVYU : BT.601 colorspace - YUV 4:2:2 planar.

    NVBUF_COLOR_FORMAT_YVYU_ER : BT.601 colorspace - YUV ER 4:2:2 planar.

    NVBUF_COLOR_FORMAT_YUV444 : BT.601 colorspace - YUV444 multi-planar.

    NVBUF_COLOR_FORMAT_RGBA : RGBA-8-8-8-8 single plane.

    NVBUF_COLOR_FORMAT_BGRA : BGRA-8-8-8-8 single plane.

    NVBUF_COLOR_FORMAT_ARGB : ARGB-8-8-8-8 single plane.

    NVBUF_COLOR_FORMAT_ABGR : ABGR-8-8-8-8 single plane.

    NVBUF_COLOR_FORMAT_RGBx : RGBx-8-8-8-8 single plane.

    NVBUF_COLOR_FORMAT_BGRx : BGRx-8-8-8-8 single plane.

    NVBUF_COLOR_FORMAT_xRGB : xRGB-8-8-8-8 single plane.

    NVBUF_COLOR_FORMAT_xBGR : xBGR-8-8-8-8 single plane.

    NVBUF_COLOR_FORMAT_RGB : RGB-8-8-8 single plane.

    NVBUF_COLOR_FORMAT_BGR : BGR-8-8-8 single plane.

    NVBUF_COLOR_FORMAT_NV12_10LE : BT.601 colorspace - Y/CbCr 4:2:0 10-bit multi-planar.

    NVBUF_COLOR_FORMAT_NV12_12LE : BT.601 colorspace - Y/CbCr 4:2:0 12-bit multi-planar.

    NVBUF_COLOR_FORMAT_YUV420_709 : BT.709 colorspace - YUV420 multi-planar.

    NVBUF_COLOR_FORMAT_YUV420_709_ER : BT.709 colorspace - YUV420 ER multi-planar.

    NVBUF_COLOR_FORMAT_NV12_709 : BT.709 colorspace - Y/CbCr 4:2:0 multi-planar.

    NVBUF_COLOR_FORMAT_NV12_709_ER : BT.709 colorspace - Y/CbCr ER 4:2:0 multi-planar.

    NVBUF_COLOR_FORMAT_YUV420_2020 : BT.2020 colorspace - YUV420 multi-planar.

    NVBUF_COLOR_FORMAT_NV12_2020 : BT.2020 colorspace - Y/CbCr 4:2:0 multi-planar.

    NVBUF_COLOR_FORMAT_NV12_10LE_ER : Specifies BT.601 colorspace - Y/CbCr ER 4:2:0
    10-bit multi-planar.

    NVBUF_COLOR_FORMAT_NV12_10LE_709 : Specifies BT.709 colorspace - Y/CbCr 4:2:0 10-bit
     multi-planar.

    NVBUF_COLOR_FORMAT_NV12_10LE_709_ER : Specifies BT.709 colorspace - Y/CbCr ER 4:2:0
    10-bit multi-planar.

    NVBUF_COLOR_FORMAT_NV12_10LE_2020 : Specifies BT.2020 colorspace - Y/CbCr 4:2:0
    10-bit multi-planar.

    NVBUF_COLOR_FORMAT_SIGNED_R16G16 : Specifies color format for packed 2 signed shorts

    NVBUF_COLOR_FORMAT_LAST : NVBUF_COLOR_FORMAT_LAST
    """

    NVBUF_COLOR_FORMAT_ABGR: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_ABGR
    NVBUF_COLOR_FORMAT_ARGB: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_ARGB
    NVBUF_COLOR_FORMAT_BGR: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_BGR
    NVBUF_COLOR_FORMAT_BGRA: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_BGRA
    NVBUF_COLOR_FORMAT_BGRx: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_BGRx
    NVBUF_COLOR_FORMAT_GRAY8: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_GRAY8
    NVBUF_COLOR_FORMAT_INVALID: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_INVALID
    NVBUF_COLOR_FORMAT_LAST: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_LAST
    NVBUF_COLOR_FORMAT_NV12: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12
    NVBUF_COLOR_FORMAT_NV12_10LE: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE
    NVBUF_COLOR_FORMAT_NV12_10LE_2020: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE_2020
    NVBUF_COLOR_FORMAT_NV12_10LE_709: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE_709
    NVBUF_COLOR_FORMAT_NV12_10LE_709_ER: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE_709_ER
    NVBUF_COLOR_FORMAT_NV12_10LE_ER: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE_ER
    NVBUF_COLOR_FORMAT_NV12_12LE: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_12LE
    NVBUF_COLOR_FORMAT_NV12_2020: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_2020
    NVBUF_COLOR_FORMAT_NV12_709: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_709
    NVBUF_COLOR_FORMAT_NV12_709_ER: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_709_ER
    NVBUF_COLOR_FORMAT_NV12_ER: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_ER
    NVBUF_COLOR_FORMAT_NV21: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV21
    NVBUF_COLOR_FORMAT_NV21_ER: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV21_ER
    NVBUF_COLOR_FORMAT_RGB: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_RGB
    NVBUF_COLOR_FORMAT_RGBA: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_RGBA
    NVBUF_COLOR_FORMAT_RGBx: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_RGBx
    NVBUF_COLOR_FORMAT_SIGNED_R16G16: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_SIGNED_R16G16
    NVBUF_COLOR_FORMAT_UYVY: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_UYVY
    NVBUF_COLOR_FORMAT_UYVY_ER: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_UYVY_ER
    NVBUF_COLOR_FORMAT_VYUY: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_VYUY
    NVBUF_COLOR_FORMAT_VYUY_ER: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_VYUY_ER
    NVBUF_COLOR_FORMAT_YUV420: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420
    NVBUF_COLOR_FORMAT_YUV420_2020: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420_2020
    NVBUF_COLOR_FORMAT_YUV420_709: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420_709
    NVBUF_COLOR_FORMAT_YUV420_709_ER: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420_709_ER
    NVBUF_COLOR_FORMAT_YUV420_ER: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420_ER
    NVBUF_COLOR_FORMAT_YUV444: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV444
    NVBUF_COLOR_FORMAT_YUYV: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUYV
    NVBUF_COLOR_FORMAT_YUYV_ER: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUYV_ER
    NVBUF_COLOR_FORMAT_YVU420: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YVU420
    NVBUF_COLOR_FORMAT_YVU420_ER: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YVU420_ER
    NVBUF_COLOR_FORMAT_YVYU: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YVYU
    NVBUF_COLOR_FORMAT_YVYU_ER: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YVYU_ER
    NVBUF_COLOR_FORMAT_xBGR: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_xBGR
    NVBUF_COLOR_FORMAT_xRGB: typing.ClassVar[
        NvBufSurfaceColorFormat
    ]  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_xRGB
    __members__: typing.ClassVar[dict[str, NvBufSurfaceColorFormat]]  # value = {

    # 'NVBUF_COLOR_FORMAT_INVALID': NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_INVALID,
    # 'NVBUF_COLOR_FORMAT_GRAY8': NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_GRAY8,
    # 'NVBUF_COLOR_FORMAT_YUV420': NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420,
    # 'NVBUF_COLOR_FORMAT_YVU420': NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YVU420,
    # 'NVBUF_COLOR_FORMAT_YUV420_ER':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420_ER,
    # 'NVBUF_COLOR_FORMAT_YVU420_ER':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YVU420_ER, 'NVBUF_COLOR_FORMAT_NV12':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12, 'NVBUF_COLOR_FORMAT_NV12_ER':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_ER, 'NVBUF_COLOR_FORMAT_NV21':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV21, 'NVBUF_COLOR_FORMAT_NV21_ER':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV21_ER, 'NVBUF_COLOR_FORMAT_UYVY':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_UYVY, 'NVBUF_COLOR_FORMAT_UYVY_ER':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_UYVY_ER, 'NVBUF_COLOR_FORMAT_VYUY':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_VYUY, 'NVBUF_COLOR_FORMAT_VYUY_ER':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_VYUY_ER, 'NVBUF_COLOR_FORMAT_YUYV':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUYV, 'NVBUF_COLOR_FORMAT_YUYV_ER':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUYV_ER, 'NVBUF_COLOR_FORMAT_YVYU':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YVYU, 'NVBUF_COLOR_FORMAT_YVYU_ER':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YVYU_ER,
    # 'NVBUF_COLOR_FORMAT_YUV444': NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV444,
    # 'NVBUF_COLOR_FORMAT_RGBA': NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_RGBA,
    # 'NVBUF_COLOR_FORMAT_BGRA': NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_BGRA,
    # 'NVBUF_COLOR_FORMAT_ARGB': NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_ARGB,
    # 'NVBUF_COLOR_FORMAT_ABGR': NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_ABGR,
    # 'NVBUF_COLOR_FORMAT_RGBx': NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_RGBx,
    # 'NVBUF_COLOR_FORMAT_BGRx': NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_BGRx,
    # 'NVBUF_COLOR_FORMAT_xRGB': NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_xRGB,
    # 'NVBUF_COLOR_FORMAT_xBGR': NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_xBGR,
    # 'NVBUF_COLOR_FORMAT_RGB': NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_RGB,
    # 'NVBUF_COLOR_FORMAT_BGR': NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_BGR,
    # 'NVBUF_COLOR_FORMAT_NV12_10LE':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE,
    # 'NVBUF_COLOR_FORMAT_NV12_12LE':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_12LE,
    # 'NVBUF_COLOR_FORMAT_YUV420_709':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420_709,
    # 'NVBUF_COLOR_FORMAT_YUV420_709_ER':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420_709_ER,
    # 'NVBUF_COLOR_FORMAT_NV12_709':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_709,
    # 'NVBUF_COLOR_FORMAT_NV12_709_ER':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_709_ER,
    # 'NVBUF_COLOR_FORMAT_YUV420_2020':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420_2020,
    # 'NVBUF_COLOR_FORMAT_NV12_2020':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_2020,
    # 'NVBUF_COLOR_FORMAT_NV12_10LE_ER':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE_ER,
    # 'NVBUF_COLOR_FORMAT_NV12_10LE_709':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE_709,
    # 'NVBUF_COLOR_FORMAT_NV12_10LE_709_ER':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE_709_ER,
    # 'NVBUF_COLOR_FORMAT_NV12_10LE_2020':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE_2020,
    # 'NVBUF_COLOR_FORMAT_SIGNED_R16G16':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_SIGNED_R16G16,
    # 'NVBUF_COLOR_FORMAT_LAST': NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_LAST}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str"""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvBufSurfaceColorFormat, arg0: int) -> None"""

    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...


class NvBufSurfaceCreateParams:
    def __init__(self) -> None: ...
    @property
    def colorFormat(self) -> NvBufSurfaceColorFormat:
        """ColorFormat"""

    @property
    def gpuId(self) -> int:
        """GpuId"""

    @property
    def height(self) -> int:
        """Height"""

    @property
    def isContiguous(self) -> bool:
        """IsContiguous"""

    @property
    def layout(self) -> NvBufSurfaceLayout:
        """Layout"""

    @property
    def memType(self) -> NvBufSurfaceMemType:
        """MemType"""

    @property
    def size(self) -> int:
        """Size"""

    @property
    def width(self) -> int:
        """Width"""


class NvBufSurfaceLayout:
    """Members:

    NVBUF_LAYOUT_PITCH : Pitch Layout.

    NVBUF_LAYOUT_BLOCK_LINEAR : Block Linear Layout.
    """

    NVBUF_LAYOUT_BLOCK_LINEAR: typing.ClassVar[
        NvBufSurfaceLayout
    ]  # value = NvBufSurfaceLayout.NVBUF_LAYOUT_BLOCK_LINEAR
    NVBUF_LAYOUT_PITCH: typing.ClassVar[
        NvBufSurfaceLayout
    ]  # value = NvBufSurfaceLayout.NVBUF_LAYOUT_PITCH
    __members__: typing.ClassVar[
        dict[str, NvBufSurfaceLayout]
    ]  # value = {'NVBUF_LAYOUT_PITCH': NvBufSurfaceLayout.NVBUF_LAYOUT_PITCH,

    # 'NVBUF_LAYOUT_BLOCK_LINEAR': NvBufSurfaceLayout.NVBUF_LAYOUT_BLOCK_LINEAR}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str"""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvBufSurfaceLayout, arg0: int) -> None"""

    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...


class NvBufSurfaceMappedAddr:
    def __init__(self) -> None: ...
    @property
    def addr(self) -> numpy.ndarray:
        """Addr"""

    @addr.setter
    def addr(self) -> None: ...
    @property
    def eglImage(self) -> typing.Any:
        """EglImage"""


class NvBufSurfaceMemMapFlags:
    """Members:

    NVBUF_MAP_READ : NVBUF_MAP_READ

    NVBUF_MAP_WRITE : NVBUF_MAP_WRITE

    NVBUF_MAP_READ_WRITE : NVBUF_MAP_READ_WRITE
    """

    NVBUF_MAP_READ: typing.ClassVar[
        NvBufSurfaceMemMapFlags
    ]  # value = NvBufSurfaceMemMapFlags.NVBUF_MAP_READ
    NVBUF_MAP_READ_WRITE: typing.ClassVar[
        NvBufSurfaceMemMapFlags
    ]  # value = NvBufSurfaceMemMapFlags.NVBUF_MAP_READ_WRITE
    NVBUF_MAP_WRITE: typing.ClassVar[
        NvBufSurfaceMemMapFlags
    ]  # value = NvBufSurfaceMemMapFlags.NVBUF_MAP_WRITE
    __members__: typing.ClassVar[
        dict[str, NvBufSurfaceMemMapFlags]
    ]  # value = {'NVBUF_MAP_READ': NvBufSurfaceMemMapFlags.NVBUF_MAP_READ,

    # 'NVBUF_MAP_WRITE': NvBufSurfaceMemMapFlags.NVBUF_MAP_WRITE,
    # 'NVBUF_MAP_READ_WRITE': NvBufSurfaceMemMapFlags.NVBUF_MAP_READ_WRITE}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str"""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvBufSurfaceMemMapFlags, arg0: int) -> None"""

    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...


class NvBufSurfaceMemType:
    """Members:

    NVBUF_MEM_DEFAULT : NVBUF_MEM_CUDA_DEVICE type for dGpu and NVBUF_MEM_SURFACE_ARRAY
    ype for Jetson.

    NVBUF_MEM_CUDA_PINNED : CUDA Host memory type.

    NVBUF_MEM_CUDA_DEVICE : CUDA Device memory type.

    NVBUF_MEM_CUDA_UNIFIED : CUDA Unified memory type.

    NVBUF_MEM_SURFACE_ARRAY : NVRM Surface Array type - valid only for Jetson.

    NVBUF_MEM_HANDLE : NVRM Handle type - valid only for Jetson.

    NVBUF_MEM_SYSTEM : NVRM Handle type - valid only for Jetson.
    """

    NVBUF_MEM_CUDA_DEVICE: typing.ClassVar[
        NvBufSurfaceMemType
    ]  # value = NvBufSurfaceMemType.NVBUF_MEM_CUDA_DEVICE
    NVBUF_MEM_CUDA_PINNED: typing.ClassVar[
        NvBufSurfaceMemType
    ]  # value = NvBufSurfaceMemType.NVBUF_MEM_CUDA_PINNED
    NVBUF_MEM_CUDA_UNIFIED: typing.ClassVar[
        NvBufSurfaceMemType
    ]  # value = NvBufSurfaceMemType.NVBUF_MEM_CUDA_UNIFIED
    NVBUF_MEM_DEFAULT: typing.ClassVar[
        NvBufSurfaceMemType
    ]  # value = NvBufSurfaceMemType.NVBUF_MEM_DEFAULT
    NVBUF_MEM_HANDLE: typing.ClassVar[
        NvBufSurfaceMemType
    ]  # value = NvBufSurfaceMemType.NVBUF_MEM_HANDLE
    NVBUF_MEM_SURFACE_ARRAY: typing.ClassVar[
        NvBufSurfaceMemType
    ]  # value = NvBufSurfaceMemType.NVBUF_MEM_SURFACE_ARRAY
    NVBUF_MEM_SYSTEM: typing.ClassVar[
        NvBufSurfaceMemType
    ]  # value = NvBufSurfaceMemType.NVBUF_MEM_SYSTEM
    __members__: typing.ClassVar[
        dict[str, NvBufSurfaceMemType]
    ]  # value = {'NVBUF_MEM_DEFAULT': NvBufSurfaceMemType.NVBUF_MEM_DEFAULT,

    # 'NVBUF_MEM_CUDA_PINNED': NvBufSurfaceMemType.NVBUF_MEM_CUDA_PINNED,
    # 'NVBUF_MEM_CUDA_DEVICE': NvBufSurfaceMemType.NVBUF_MEM_CUDA_DEVICE,
    # 'NVBUF_MEM_CUDA_UNIFIED': NvBufSurfaceMemType.NVBUF_MEM_CUDA_UNIFIED,
    # 'NVBUF_MEM_SURFACE_ARRAY': NvBufSurfaceMemType.NVBUF_MEM_SURFACE_ARRAY,
    # 'NVBUF_MEM_HANDLE': NvBufSurfaceMemType.NVBUF_MEM_HANDLE,
    # 'NVBUF_MEM_SYSTEM': NvBufSurfaceMemType.NVBUF_MEM_SYSTEM}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str"""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvBufSurfaceMemType, arg0: int) -> None"""

    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...


class NvBufSurfaceParams:
    def __init__(self) -> None: ...
    @property
    def bufferDesc(self) -> int:
        """BufferDesc"""

    @property
    def colorFormat(self) -> NvBufSurfaceColorFormat:
        """ColorFormat"""

    @property
    def dataPtr(self) -> typing.Any:
        """DataPtr"""

    @property
    def dataSize(self) -> int:
        """DataSize"""

    @property
    def height(self) -> int:
        """Height"""

    @property
    def layout(self) -> NvBufSurfaceLayout:
        """Layout"""

    @property
    def mappedAddr(self) -> NvBufSurfaceMappedAddr:
        """MappedAddr"""

    @property
    def pitch(self) -> int:
        """Pitch"""

    @property
    def planeParams(self) -> NvBufSurfacePlaneParams:
        """PlaneParams"""

    @property
    def width(self) -> int:
        """Width"""


class NvBufSurfacePlaneParams:
    def __init__(self) -> None: ...
    @property
    def bytesPerPix(self) -> numpy.ndarray:
        """Bytes taken for each pixel"""

    @bytesPerPix.setter
    def bytesPerPix(self) -> None: ...
    @property
    def height(self) -> numpy.ndarray:
        """Height of planes"""

    @height.setter
    def height(self) -> None: ...
    @property
    def num_planes(self) -> int:
        """num_planes"""

    @num_planes.setter
    def num_planes(self, arg0: int) -> None: ...
    @property
    def offset(self) -> numpy.ndarray:
        """Offsets of planes in bytes"""

    @offset.setter
    def offset(self) -> None: ...
    @property
    def pitch(self) -> numpy.ndarray:
        """Pitch of planes in bytes"""

    @pitch.setter
    def pitch(self) -> None: ...
    @property
    def psize(self) -> numpy.ndarray:
        """Ize of planes in bytes"""

    @psize.setter
    def psize(self) -> None: ...
    @property
    def width(self) -> numpy.ndarray:
        """Width of planes"""

    @width.setter
    def width(self) -> None: ...


class NvDsAnalyticsFrameMeta:
    """Holds a set of nvdsanalytics object level metadata."""

    @staticmethod
    def cast(arg0: capsule[NvDsAnalyticsFrameMeta]) -> NvDsAnalyticsFrameMeta:
        """Cast given object/data to pyds.NvDsAnalyticsFrameMetaDoc, call
        pyds.NvDsAnalyticsFrameMetaDoc.cast(data)
        """

    def __init__(self) -> None: ...
    @property
    def objCnt(self) -> dict[int, int]:
        """Holds a map of total count of objects for each class ID, can be accessed
        using key, value pair; where key is class ID
        """

    @objCnt.setter
    def objCnt(self, arg0: dict[int, int]) -> None: ...
    @property
    def objInROIcnt(self) -> dict[str, int]:
        """Holds a map of total count of valid objects in ROI  for configured ROIs,which
        can be accessed using key, value pair; where key is the ROI label
        """

    @objInROIcnt.setter
    def objInROIcnt(self, arg0: dict[str, int]) -> None: ...
    @property
    def objLCCumCnt(self) -> dict[str, int]:
        """Holds a map of total cumulative count of Line crossing  for configured lines,
        can be accessed using key, value pair; where key is the line crossing label
        """

    @objLCCumCnt.setter
    def objLCCumCnt(self, arg0: dict[str, int]) -> None: ...
    @property
    def objLCCurrCnt(self) -> dict[str, int]:
        """Holds a map of total count of Line crossing in current frame for configured
        lines,which can be accessed using key, value pair; where key is the line
        crossing label
        """

    @objLCCurrCnt.setter
    def objLCCurrCnt(self, arg0: dict[str, int]) -> None: ...
    @property
    def ocStatus(self) -> dict[str, bool]:
        """Holds a map of boolean status of overcrowding for configured ROIs,which can
        be accessed using key, value pair; where key is the ROI label
        """

    @ocStatus.setter
    def ocStatus(self, arg0: dict[str, bool]) -> None: ...
    @property
    def unique_id(self) -> int:
        """Holds unique identifier for nvdsanalytics instance"""

    @unique_id.setter
    def unique_id(self, arg0: int) -> None: ...


class NvDsAnalyticsObjInfo:
    """Holds a set of nvdsanalytics object level metadata."""

    @staticmethod
    def cast(arg0: capsule[NvDsAnalyticsObjInfo]) -> NvDsAnalyticsObjInfo:
        """Cast given object/data to pyds.NvDsAnalyticsObjInfoDoc, call
        pyds.NvDsAnalyticsObjInfoDoc.cast(data)
        """

    def __init__(self) -> None: ...
    @property
    def dirStatus(self) -> str:
        """Holds the direction string for the tracked object"""

    @dirStatus.setter
    def dirStatus(self, arg0: str) -> None: ...
    @property
    def lcStatus(self) -> list[str]:
        """Holds the array of line crossing labels which object has crossed"""

    @lcStatus.setter
    def lcStatus(self, arg0: list[str]) -> None: ...
    @property
    def ocStatus(self) -> list[str]:
        """Holds the array  of OverCrowding labels in which object is present"""

    @ocStatus.setter
    def ocStatus(self, arg0: list[str]) -> None: ...
    @property
    def roiStatus(self) -> list[str]:
        """Holds the array of ROI labels in which object is present"""

    @roiStatus.setter
    def roiStatus(self, arg0: list[str]) -> None: ...
    @property
    def unique_id(self) -> int:
        """Holds unique identifier for nvdsanalytics instance"""

    @unique_id.setter
    def unique_id(self, arg0: int) -> None: ...


class NvDsBaseMeta:
    """Holds information about base metadata of given metadata type."""

    def __init__(self) -> None: ...
    @property
    def batch_meta(self) -> NvDsBatchMeta:
        """batch_meta"""

    @batch_meta.setter
    def batch_meta(self, arg0: NvDsBatchMeta) -> None: ...
    @property
    def meta_type(self) -> NvDsMetaType:
        """Metadata type of the given element"""

    @meta_type.setter
    def meta_type(self, arg0: NvDsMetaType) -> None: ...
    @property
    def uContext(self) -> typing.Any:
        """User context"""

    @uContext.setter
    def uContext(self, arg0: typing.Any) -> None: ...


class NvDsBatchMeta:
    """Holds information a formed batched containing the frames from different
    sources.
    """

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsBatchMeta]) -> NvDsBatchMeta:
        """Cast given object/data to pyds.NvDsBatchMeta, call
        pyds.NvDsBatchMeta.cast(data)
        """

    @typing.overload
    def cast(self: int) -> NvDsBatchMeta:
        """Cast given object/data to pyds.NvDsBatchMeta, call
        pyds.NvDsBatchMeta.cast(data)
        """

    @property
    def base_meta(self) -> NvDsBaseMeta:
        """base_meta"""

    @base_meta.setter
    def base_meta(self, arg0: NvDsBaseMeta) -> None: ...
    @property
    def batch_user_meta_list(self) -> typing.Optional[GList[NvDsUserMeta]]:
        """A list of items of type pyds.NvDsUserMeta in use in the current batch"""

    @batch_user_meta_list.setter
    def batch_user_meta_list(
        self, arg0: typing.Optional[GList[NvDsUserMeta]]
    ) -> None: ...
    @property
    def classifier_meta_pool(self) -> NvDsMetaPool:
        """Pool of type pyds.NvDsClassifierMeta"""

    @classifier_meta_pool.setter
    def classifier_meta_pool(self, arg0: NvDsMetaPool) -> None: ...
    @property
    def display_meta_pool(self) -> NvDsMetaPool:
        """A pool of type pyds.NvDsDisplayMeta"""

    @display_meta_pool.setter
    def display_meta_pool(self, arg0: NvDsMetaPool) -> None: ...
    @property
    def frame_meta_list(self) -> typing.Optional[GList[NvDsFrameMeta]]:
        """A list of items of type pyds.NvDsFrameMeta in use in the current batch"""

    @frame_meta_list.setter
    def frame_meta_list(self, arg0: typing.Optional[GList[NvDsFrameMeta]]) -> None: ...
    @property
    def frame_meta_pool(self) -> NvDsMetaPool:
        """Pool of type pyds.NvDsFrameMeta"""

    @frame_meta_pool.setter
    def frame_meta_pool(self, arg0: NvDsMetaPool) -> None: ...
    @property
    def label_info_meta_pool(self) -> NvDsMetaPool:
        """A pool of type pyds.NvDsLabelInfo"""

    @label_info_meta_pool.setter
    def label_info_meta_pool(self, arg0: NvDsMetaPool) -> None: ...
    @property
    def max_frames_in_batch(self) -> int:
        """Maximum number of frames those can be present the batch"""

    @max_frames_in_batch.setter
    def max_frames_in_batch(self, arg0: int) -> None: ...
    @property
    def meta_mutex(self) -> GLib.RecMutex:
        """Lock to be taken before accessing metadata to avoid simultaneous update of
        same metadata by multiple components
        """

    @meta_mutex.setter
    def meta_mutex(self, arg0: GLib.RecMutex) -> None: ...
    @property
    def misc_batch_info(self) -> numpy.ndarray:
        """For additional user specific batch info"""

    @misc_batch_info.setter
    def misc_batch_info(self) -> None: ...
    @property
    def num_frames_in_batch(self) -> int:
        """Number of frames present in the current batch"""

    @num_frames_in_batch.setter
    def num_frames_in_batch(self, arg0: int) -> None: ...
    @property
    def obj_meta_pool(self) -> NvDsMetaPool:
        """Pool of type pyds.NvDsObjMeta"""

    @obj_meta_pool.setter
    def obj_meta_pool(self, arg0: NvDsMetaPool) -> None: ...
    @property
    def reserved(self) -> numpy.ndarray:
        """Reserved"""

    @reserved.setter
    def reserved(self) -> None: ...
    @property
    def user_meta_pool(self) -> NvDsMetaPool:
        """A pool of type pyds.NvDsUserMeta"""

    @user_meta_pool.setter
    def user_meta_pool(self, arg0: NvDsMetaPool) -> None: ...


class NvDsClassifierMeta:
    """Holds information of classifier metadata in the object"""

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsClassifierMeta]) -> NvDsClassifierMeta:
        """Cast given object/data to pyds.NvDsClassifierMeta, call
        pyds.NvDsClassifierMeta.cast(data)
        """

    @typing.overload
    def cast(self: int) -> NvDsClassifierMeta:
        """Cast given object/data to pyds.NvDsClassifierMeta, call
        pyds.NvDsClassifierMeta.cast(data)
        """

    @property
    def base_meta(self) -> NvDsBaseMeta:
        """base_meta"""

    @base_meta.setter
    def base_meta(self, arg0: NvDsBaseMeta) -> None: ...
    @property
    def label_info_list(self) -> typing.Optional[GList[NvDsLabelInfo]]:
        """List of label objects of the given class"""

    @label_info_list.setter
    def label_info_list(self, arg0: typing.Optional[GList[NvDsLabelInfo]]) -> None: ...
    @property
    def num_labels(self) -> int:
        """Number of outputs/labels of the classifier"""

    @num_labels.setter
    def num_labels(self, arg0: int) -> None: ...
    @property
    def unique_component_id(self) -> int:
        """Unique component id that attaches NvDsClassifierMeta metadata"""

    @unique_component_id.setter
    def unique_component_id(self, arg0: int) -> None: ...


class NvDsComp_BboxInfo:
    """Holds unclipped positional bounding box coordinates of the object processed by
    the component.
    """

    def __init__(self) -> None: ...
    @property
    def org_bbox_coords(self) -> NvBbox_Coords:
        """org_bbox_coords"""

    @org_bbox_coords.setter
    def org_bbox_coords(self, arg0: NvBbox_Coords) -> None: ...


class NvDsCoordinate:
    """Hold coordinate parameters."""

    def __init__(self) -> None: ...
    @property
    def x(self) -> float:
        """X"""

    @x.setter
    def x(self, arg0: float) -> None: ...
    @property
    def y(self) -> float:
        """Y"""

    @y.setter
    def y(self, arg0: float) -> None: ...
    @property
    def z(self) -> float:
        """Z"""

    @z.setter
    def z(self, arg0: float) -> None: ...


class NvDsDisplayMeta:
    """Holds information of display metadata that user can specify in the frame"""

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsDisplayMeta]) -> NvDsDisplayMeta:
        """Cast given object/data to pyds.NvDsDisplayMeta, call
        pyds.NvDsDisplayMeta.cast(data)
        """

    @typing.overload
    def cast(self: int) -> NvDsDisplayMeta:
        """Cast given object/data to pyds.NvDsDisplayMeta, call
        pyds.NvDsDisplayMeta.cast(data)
        """

    @property
    def arrow_params(self) -> list[NvOSD_ArrowParams]:
        """Parameters of the line of polygon that user can draw in the frame. e.g. to
        set ROI in the frame by specifying the lines.  Refer pyds.NvOSD_RectParams
        """

    @property
    def base_meta(self) -> NvDsBaseMeta:
        """base_meta"""

    @base_meta.setter
    def base_meta(self, arg0: NvDsBaseMeta) -> None: ...
    @property
    def circle_params(self) -> list[NvOSD_CircleParams]:
        """Parameters of the line of polygon that user can draw in the frame. e.g. to
        set ROI in the frame by specifying the lines.  Refer pyds.NvOSD_RectParams
        """

    @property
    def line_params(self) -> list[NvOSD_LineParams]:
        """Parameters of the line of polygon that user can draw in the frame. e.g. to
        set ROI in the frame by specifying the lines.  Refer pyds.NvOSD_RectParams
        """

    @property
    def misc_osd_data(self) -> numpy.ndarray:
        """misc_osd_data"""

    @misc_osd_data.setter
    def misc_osd_data(self) -> None: ...
    @property
    def num_arrows(self) -> int:
        """Holds the number of arrows described."""

    @num_arrows.setter
    def num_arrows(self, arg0: int) -> None: ...
    @property
    def num_circles(self) -> int:
        """Holds the number of circles described."""

    @num_circles.setter
    def num_circles(self, arg0: int) -> None: ...
    @property
    def num_labels(self) -> int:
        """Number of labels/strings present in display meta"""

    @num_labels.setter
    def num_labels(self, arg0: int) -> None: ...
    @property
    def num_lines(self) -> int:
        """Number of lines present in display meta"""

    @num_lines.setter
    def num_lines(self, arg0: int) -> None: ...
    @property
    def num_rects(self) -> int:
        """Number of rectangles present in display meta"""

    @num_rects.setter
    def num_rects(self, arg0: int) -> None: ...
    @property
    def rect_params(self) -> list[NvOSD_RectParams]:
        """Structure containing the positional parameters to overlay borders or
        semi-transparent rectangles as required by the user in the frame Refer
        pyds.NvOSD_RectParams
        """

    @property
    def reserved(self) -> numpy.ndarray:
        """Reserved"""

    @reserved.setter
    def reserved(self) -> None: ...
    @property
    def text_params(self) -> list[NvOSD_TextParams]:
        """Text describing the user defined string can be overlayed using this object.
        @see pyds.NvOSD_TextParams
        """


class NvDsEvent:
    """Holds event information."""

    def __init__(self) -> None: ...
    @property
    def eventType(self) -> NvDsEventType:
        """Type of event"""

    @eventType.setter
    def eventType(self, arg0: NvDsEventType) -> None: ...
    @property
    def metadata(self) -> NvDsEventMsgMeta:
        """Object of event meta data."""

    @metadata.setter
    def metadata(self, arg0: NvDsEventMsgMeta) -> None: ...


class NvDsEventMsgMeta:
    """Holds face parameters."""

    extMsgSize: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsEventMsgMeta]) -> NvDsEventMsgMeta:
        """Casts to NvDsEventMsgMeta object, call pyds.NvDsEventMsgMeta(data)"""

    @typing.overload
    def cast(self: int) -> NvDsEventMsgMeta:
        """Casts to NvDsEventMsgMeta object, call pyds.NvDsEventMsgMeta(data)"""

    @property
    def bbox(self) -> NvDsRect:
        """Bounding box of object"""

    @bbox.setter
    def bbox(self, arg0: NvDsRect) -> None: ...
    @property
    def componentId(self) -> int:
        """Id of component that generated this event"""

    @componentId.setter
    def componentId(self, arg0: int) -> None: ...
    @property
    def confidence(self) -> float:
        """Confidence of inference"""

    @confidence.setter
    def confidence(self, arg0: float) -> None: ...
    @property
    def coordinate(self) -> NvDsCoordinate:
        """Coordinate of object"""

    @coordinate.setter
    def coordinate(self, arg0: NvDsCoordinate) -> None: ...
    @property
    def extMsg(self) -> typing.Any:
        """To extend the event message meta data. This can be used for custom values
        that can't be accommodated in the existing fields OR if object(vehicle, person,
        face etc.) specific values needs to be attached.
        """

    @extMsg.setter
    def extMsg(self, arg0: typing.Any) -> None: ...
    @property
    def frameId(self) -> int:
        """Video frame id of this event"""

    @frameId.setter
    def frameId(self, arg0: int) -> None: ...
    @property
    def location(self) -> NvDsGeoLocation:
        """Geo-location of object"""

    @location.setter
    def location(self, arg0: NvDsGeoLocation) -> None: ...
    @property
    def moduleId(self) -> int:
        """Id of analytics module that generated the event"""

    @moduleId.setter
    def moduleId(self, arg0: int) -> None: ...
    @property
    def objClassId(self) -> int:
        """Class id of object"""

    @objClassId.setter
    def objClassId(self, arg0: int) -> None: ...
    @property
    def objSignature(self) -> NvDsObjectSignature:
        """Signature of object"""

    @objSignature.setter
    def objSignature(self, arg0: NvDsObjectSignature) -> None: ...
    @property
    def objType(self) -> NvDsObjectType:
        """Type of object"""

    @objType.setter
    def objType(self, arg0: NvDsObjectType) -> None: ...
    @property
    def objectId(self) -> int:
        """Id of detected / inferred object"""

    @objectId.setter
    def objectId(self, arg1: str) -> None: ...
    @property
    def otherAttrs(self) -> int:
        """Other attributes associated with the object"""

    @otherAttrs.setter
    def otherAttrs(self, arg1: str) -> None: ...
    @property
    def placeId(self) -> int:
        """Id of place related to the object"""

    @placeId.setter
    def placeId(self, arg0: int) -> None: ...
    @property
    def sensorId(self) -> int:
        """Id of sensor that generated the event"""

    @sensorId.setter
    def sensorId(self, arg0: int) -> None: ...
    @property
    def sensorStr(self) -> int:
        """Identity string of sensor"""

    @sensorStr.setter
    def sensorStr(self, arg1: str) -> None: ...
    @property
    def trackingId(self) -> int:
        """Tracking id of object"""

    @trackingId.setter
    def trackingId(self, arg0: int) -> None: ...
    @property
    def ts(self) -> int:
        """Time stamp of generated event"""

    @ts.setter
    def ts(self, arg1: int) -> None: ...
    @property
    def type(self) -> NvDsEventType:
        """Type of event"""

    @type.setter
    def type(self, arg0: NvDsEventType) -> None: ...
    @property
    def videoPath(self) -> int:
        """Name of video file"""

    @videoPath.setter
    def videoPath(self, arg1: str) -> None: ...


class NvDsEventType:
    """Event type flags.

    Members:

      NVDS_EVENT_ENTRY : NVDS_EVENT_ENTRY

      NVDS_EVENT_EXIT : NVDS_EVENT_EXIT

      NVDS_EVENT_MOVING : NVDS_EVENT_MOVING

      NVDS_EVENT_STOPPED : NVDS_EVENT_STOPPED

      NVDS_EVENT_EMPTY : NVDS_EVENT_EMPTY

      NVDS_EVENT_PARKED : NVDS_EVENT_PARKED

      NVDS_EVENT_RESET : NVDS_EVENT_RESET

      NVDS_EVENT_RESERVED : Reserved for future use. Use value greater than this for
      custom events.

      NVDS_EVENT_CUSTOM : NVDS_EVENT_CUSTOM

      NVDS_EVENT_FORCE32 : NVDS_EVENT_FORCE32
    """

    NVDS_EVENT_CUSTOM: typing.ClassVar[
        NvDsEventType
    ]  # value = NvDsEventType.NVDS_EVENT_CUSTOM
    NVDS_EVENT_EMPTY: typing.ClassVar[
        NvDsEventType
    ]  # value = NvDsEventType.NVDS_EVENT_EMPTY
    NVDS_EVENT_ENTRY: typing.ClassVar[
        NvDsEventType
    ]  # value = NvDsEventType.NVDS_EVENT_ENTRY
    NVDS_EVENT_EXIT: typing.ClassVar[
        NvDsEventType
    ]  # value = NvDsEventType.NVDS_EVENT_EXIT
    NVDS_EVENT_FORCE32: typing.ClassVar[
        NvDsEventType
    ]  # value = NvDsEventType.NVDS_EVENT_FORCE32
    NVDS_EVENT_MOVING: typing.ClassVar[
        NvDsEventType
    ]  # value = NvDsEventType.NVDS_EVENT_MOVING
    NVDS_EVENT_PARKED: typing.ClassVar[
        NvDsEventType
    ]  # value = NvDsEventType.NVDS_EVENT_PARKED
    NVDS_EVENT_RESERVED: typing.ClassVar[
        NvDsEventType
    ]  # value = NvDsEventType.NVDS_EVENT_RESERVED
    NVDS_EVENT_RESET: typing.ClassVar[
        NvDsEventType
    ]  # value = NvDsEventType.NVDS_EVENT_RESET
    NVDS_EVENT_STOPPED: typing.ClassVar[
        NvDsEventType
    ]  # value = NvDsEventType.NVDS_EVENT_STOPPED
    __members__: typing.ClassVar[
        dict[str, NvDsEventType]
    ]  # value = {'NVDS_EVENT_ENTRY': NvDsEventType.NVDS_EVENT_ENTRY,

    # 'NVDS_EVENT_EXIT': NvDsEventType.NVDS_EVENT_EXIT,
    # 'NVDS_EVENT_MOVING': NvDsEventType.NVDS_EVENT_MOVING,
    # 'NVDS_EVENT_STOPPED': NvDsEventType.NVDS_EVENT_STOPPED,
    # 'NVDS_EVENT_EMPTY': NvDsEventType.NVDS_EVENT_EMPTY,
    # 'NVDS_EVENT_PARKED': NvDsEventType.NVDS_EVENT_PARKED,
    # 'NVDS_EVENT_RESET': NvDsEventType.NVDS_EVENT_RESET,
    # 'NVDS_EVENT_RESERVED': NvDsEventType.NVDS_EVENT_RESERVED,
    # 'NVDS_EVENT_CUSTOM': NvDsEventType.NVDS_EVENT_CUSTOM,
    # 'NVDS_EVENT_FORCE32': NvDsEventType.NVDS_EVENT_FORCE32}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str"""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvDsEventType, arg0: int) -> None"""

    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...


class NvDsFaceObject:
    """Holds face parameters."""

    def __init__(self) -> None: ...
    @property
    def age(self) -> int:
        """Age"""

    @age.setter
    def age(self, arg0: int) -> None: ...
    @property
    def cap(self) -> int:
        """Cap"""

    @cap.setter
    def cap(self, arg1: str) -> None: ...
    @property
    def eyecolor(self) -> int:
        """Eyecolor"""

    @eyecolor.setter
    def eyecolor(self, arg1: str) -> None: ...
    @property
    def facialhair(self) -> int:
        """Facialhair"""

    @facialhair.setter
    def facialhair(self, arg1: str) -> None: ...
    @property
    def gender(self) -> int:
        """Gender"""

    @gender.setter
    def gender(self, arg1: str) -> None: ...
    @property
    def glasses(self) -> int:
        """Glasses"""

    @glasses.setter
    def glasses(self, arg1: str) -> None: ...
    @property
    def hair(self) -> int:
        """Hair"""

    @hair.setter
    def hair(self, arg1: str) -> None: ...
    @property
    def name(self) -> int:
        """Name"""

    @name.setter
    def name(self, arg1: str) -> None: ...


class NvDsFaceObjectWithExt:
    """Holds a vehicle object's parameters."""

    def __init__(self) -> None: ...
    @property
    def age(self) -> int:
        """Object holding information of person's age."""

    @age.setter
    def age(self, arg0: int) -> None: ...
    @property
    def cap(self) -> str:
        """Object holding information of the type of cap person is wearing."""

    @cap.setter
    def cap(self, arg0: str) -> None: ...
    @property
    def eyecolor(self) -> str:
        """Object holding information of person's eyecolor."""

    @eyecolor.setter
    def eyecolor(self, arg0: str) -> None: ...
    @property
    def facialhair(self) -> str:
        """Object holding information of person's age."""

    @facialhair.setter
    def facialhair(self, arg0: str) -> None: ...
    @property
    def gender(self) -> str:
        """Object holding information of person's gender."""

    @gender.setter
    def gender(self, arg0: str) -> None: ...
    @property
    def glasses(self) -> str:
        """Object holding description of the person's apparel."""

    @glasses.setter
    def glasses(self, arg0: str) -> None: ...
    @property
    def hair(self) -> str:
        """Object holding information of person's hair color."""

    @hair.setter
    def hair(self, arg0: str) -> None: ...
    @property
    def mask(self) -> typing.Optional[GList[typing.Any]]:
        """List of polygons for person mask."""

    @mask.setter
    def mask(self, arg0: typing.Optional[GList[typing.Any]]) -> None: ...
    @property
    def name(self) -> str:
        """Object holding information of persons name."""

    @name.setter
    def name(self, arg0: str) -> None: ...


class NvDsFrameMeta:
    """Holds information of frame metadata in the batch"""

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsFrameMeta]) -> NvDsFrameMeta:
        """Cast given object/data to pyds.NvDsFrameMeta, call
        pyds.NvDsFrameMeta.cast(data)
        """

    @typing.overload
    def cast(self: int) -> NvDsFrameMeta:
        """Cast given object/data to pyds.NvDsFrameMeta, call
        pyds.NvDsFrameMeta.cast(data)
        """

    @property
    def bInferDone(self) -> int:
        """Boolean indicating whether inference is performed on given frame"""

    @bInferDone.setter
    def bInferDone(self, arg0: int) -> None: ...
    @property
    def base_meta(self) -> NvDsBaseMeta:
        """Base metadata for frame"""

    @base_meta.setter
    def base_meta(self, arg0: NvDsBaseMeta) -> None: ...
    @property
    def batch_id(self) -> int:
        """Location of the frame in the batch. pyds.NvBufSurfaceParams for the frame
        will be at index batch_id in the surfaceList array of pyds.NvBufSurface.
        """

    @batch_id.setter
    def batch_id(self, arg0: int) -> None: ...
    @property
    def buf_pts(self) -> int:
        """Pts of the frame"""

    @buf_pts.setter
    def buf_pts(self, arg0: int) -> None: ...
    @property
    def display_meta_list(self) -> typing.Optional[GList[NvDsDisplayMeta]]:
        """List of objects of type pyds.NvDsDisplayMeta in use for the given frame"""

    @display_meta_list.setter
    def display_meta_list(
        self, arg0: typing.Optional[GList[NvDsDisplayMeta]]
    ) -> None: ...
    @property
    def frame_num(self) -> int:
        """Current frame number of the source"""

    @frame_num.setter
    def frame_num(self, arg0: int) -> None: ...
    @property
    def frame_user_meta_list(self) -> typing.Optional[GList[NvDsUserMeta]]:
        """List of objects of type pyds.NvDsUserMeta in use for the given frame"""

    @frame_user_meta_list.setter
    def frame_user_meta_list(
        self, arg0: typing.Optional[GList[NvDsUserMeta]]
    ) -> None: ...
    @property
    def misc_frame_info(self) -> numpy.ndarray:
        """misc_frame_info"""

    @misc_frame_info.setter
    def misc_frame_info(self) -> None: ...
    @property
    def ntp_timestamp(self) -> int:
        """ntp_timestamp"""

    @ntp_timestamp.setter
    def ntp_timestamp(self, arg0: int) -> None: ...
    @property
    def num_obj_meta(self) -> int:
        """Number of object meta elements attached to the current frame"""

    @num_obj_meta.setter
    def num_obj_meta(self, arg0: int) -> None: ...
    @property
    def num_surfaces_per_frame(self) -> int:
        """Number of surfaces present in this frame. This is required in case multiple
        surfaces per frame
        """

    @num_surfaces_per_frame.setter
    def num_surfaces_per_frame(self, arg0: int) -> None: ...
    @property
    def obj_meta_list(self) -> typing.Optional[GList[NvDsObjectMeta]]:
        """List of objects of type pyds.NvDsObjectMeta in use for the given frame"""

    @obj_meta_list.setter
    def obj_meta_list(self, arg0: typing.Optional[GList[NvDsObjectMeta]]) -> None: ...
    @property
    def pad_index(self) -> int:
        """Pad or port index of stream muxer component for the frame in the batch"""

    @pad_index.setter
    def pad_index(self, arg0: int) -> None: ...
    @property
    def reserved(self) -> numpy.ndarray:
        """Reserved"""

    @reserved.setter
    def reserved(self) -> None: ...
    @property
    def source_frame_height(self) -> int:
        """Height of the frame at the input of stream muxer"""

    @source_frame_height.setter
    def source_frame_height(self, arg0: int) -> None: ...
    @property
    def source_frame_width(self) -> int:
        """Width of the frame at the input of stream muxer"""

    @source_frame_width.setter
    def source_frame_width(self, arg0: int) -> None: ...
    @property
    def source_id(self) -> int:
        """source_id of the frame in the batch e.g. camera_id. It need not be in
        sequential order
        """

    @source_id.setter
    def source_id(self, arg0: int) -> None: ...
    @property
    def surface_index(self) -> int:
        """Surface index of sub frame. This is required in case multiple surfaces per
        frame
        """

    @surface_index.setter
    def surface_index(self, arg0: int) -> None: ...
    @property
    def surface_type(self) -> int:
        """Surface type of sub frame. This is required in case multiple surfaces per
        frame
        """

    @surface_type.setter
    def surface_type(self, arg0: int) -> None: ...


class NvDsGeoLocation:
    """Holds Geo-location parameters."""

    def __init__(self) -> None: ...
    @property
    def alt(self) -> float:
        """Alt"""

    @alt.setter
    def alt(self, arg0: float) -> None: ...
    @property
    def lat(self) -> float:
        """Lat"""

    @lat.setter
    def lat(self, arg0: float) -> None: ...
    @property
    def lon(self) -> float:
        """Lon"""

    @lon.setter
    def lon(self, arg0: float) -> None: ...


class NvDsInferAttribute:
    """Holds information about one classified attribute."""

    def __init__(self) -> None: ...
    @property
    def attributeConfidence(self) -> float:
        """Confidence level for the classified attribute."""

    @property
    def attributeLabel(self) -> str:
        """String label for the attribute. Memory for the string should not be freed."""

    @property
    def attributeValue(self) -> int:
        """Output for the label."""

    @property
    def atttributeIndex(self) -> int:
        """Index of the label. This index corresponds to the order of output layers
        specified in the outputCoverageLayerNames vector during  initialization.
        """


class NvDsInferDataType:
    """Data type of the layers.

    Members:

      FLOAT : FP32 format.

      HALF : FP16 format.

      INT8 : INT8 format.

      INT32 : INT32 format.
    """

    FLOAT: typing.ClassVar[NvDsInferDataType]  # value = NvDsInferDataType.FLOAT
    HALF: typing.ClassVar[NvDsInferDataType]  # value = NvDsInferDataType.HALF
    INT32: typing.ClassVar[NvDsInferDataType]  # value = NvDsInferDataType.INT32
    INT8: typing.ClassVar[NvDsInferDataType]  # value = NvDsInferDataType.INT8
    __members__: typing.ClassVar[
        dict[str, NvDsInferDataType]
    ]  # value = {'FLOAT': NvDsInferDataType.FLOAT, 'HALF': NvDsInferDataType.HALF,

    # 'INT8': NvDsInferDataType.INT8, 'INT32': NvDsInferDataType.INT32}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str"""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvDsInferDataType, arg0: int) -> None"""

    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...


class NvDsInferDims:
    """Specifies dimensions of a layer."""

    def __init__(self) -> None: ...
    @property
    def d(self) -> numpy.ndarray:
        """Size of the layer in each dimension."""

    @d.setter
    def d(self) -> None: ...
    @property
    def numDims(self) -> int:
        """Number of dimesions of the layer."""

    @property
    def numElements(self) -> int:
        """Number of elements in the layer including all dimensions."""


class NvDsInferDimsCHW:
    """Specifies dimensions of a layer with 3 dimensions."""

    def __init__(self) -> None: ...
    @property
    def c(self) -> int:
        """Channel count of the layer."""

    @property
    def h(self) -> int:
        """Height of the layer."""

    @property
    def w(self) -> int:
        """Width of the layer."""


class NvDsInferLayerInfo:
    """Holds information about one layer in the model."""

    def __init__(self) -> None: ...
    @property
    def bindingIndex(self) -> int:
        """TensorRT binding index of the layer."""

    @property
    def buffer(self) -> typing.Any:
        """Pointer to the buffer for the layer data."""

    @property
    def dataType(self) -> NvDsInferDataType:
        """Data type of the layer."""

    @property
    def dims(self) -> NvDsInferDims:
        """Dimensions of the layer."""

    @property
    def isInput(self) -> int:
        """Boolean indicating if the layer is an input layer. The layer is an output
        layer when the flag is set to 0.
        """

    @property
    def layerName(self) -> str:
        """Name of the layer."""


class NvDsInferNetworkInfo:
    """Holds information about the model network."""

    def __init__(self) -> None: ...
    @property
    def channels(self) -> int:
        """Number of input channels for the model."""

    @channels.setter
    def channels(self, arg0: int) -> None: ...
    @property
    def height(self) -> int:
        """Input height for the model."""

    @height.setter
    def height(self, arg0: int) -> None: ...
    @property
    def width(self) -> int:
        """Input width for the model."""

    @width.setter
    def width(self, arg0: int) -> None: ...


class NvDsInferObjectDetectionInfo:
    """Holds information about one parsed object from detector's output."""

    def __init__(self) -> None: ...
    @property
    def classId(self) -> int:
        """ID of the class to which the object belongs."""

    @classId.setter
    def classId(self, arg0: int) -> None: ...
    @property
    def detectionConfidence(self) -> float:
        """Object detection confidence. Should be a float value in the range [0,1]"""

    @detectionConfidence.setter
    def detectionConfidence(self, arg0: float) -> None: ...
    @property
    def height(self) -> float:
        """Height of the bounding box shape for the object."""

    @height.setter
    def height(self, arg0: float) -> None: ...
    @property
    def left(self) -> float:
        """Horizontal offset of the bounding box shape for the object."""

    @left.setter
    def left(self, arg0: float) -> None: ...
    @property
    def top(self) -> float:
        """Vertical offset of the bounding box shape for the object."""

    @top.setter
    def top(self, arg0: float) -> None: ...
    @property
    def width(self) -> float:
        """Width of the bounding box shape for the object."""

    @width.setter
    def width(self, arg0: float) -> None: ...


class NvDsInferSegmentationMeta:
    """Holds the segmentation model output information for one frame / one object.
    The "nvinfer" plugins adds this meta for segmentation models.
    This meta data is added as NvDsUserMeta to the frame_user_meta_list of the
    corresponding frame_meta or object_user_meta_list of the corresponding object
    with the meta_type set to NVDSINFER_SEGMENTATION_META.

    """

    def __init__(self) -> None: ...
    def cast(self: capsule[NvDsInferSegmentationMeta]) -> NvDsInferSegmentationMeta:
        """Cast given object/data to pyds.NvDsInferSegmentationMeta, call
        pyds.NvDsInferSegmentationMeta.cast(data)
        """

    @property
    def class_map(self) -> int:
        """Pointer to the array for 2D pixel class map. The output for pixel (x,y)  will
        be at index (y * width + x).
        """

    @property
    def class_probabilities_map(self) -> float:
        """Pointer to the raw array containing the probabilities. The probability for
        class c and pixel (x,y) will be at index (c * width *height + y * width + x).
        """

    @property
    def classes(self) -> int:
        """Number of classes in the segmentation output."""

    @property
    def height(self) -> int:
        """Height of the segmentation output class map."""

    @property
    def priv_data(self) -> typing.Any:
        """Private data used for the meta producer's internal memory management."""

    @property
    def width(self) -> int:
        """Width of the segmentation output class map."""


class NvDsInferTensorMeta:
    """Holds the raw tensor output information for one frame / one object. The "nvinfer"
    plugins adds this meta when the "output-tensor-meta" property  of the element
    instanceis set to TRUE.
    This meta data is added as NvDsUserMeta to the frame_user_meta_list of the
    corresponding frame_meta or object_user_meta_list of the corresponding object
    with the meta_type set to NVDSINFER_TENSOR_OUTPUT_META.

    """

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsInferTensorMeta]) -> NvDsInferTensorMeta:
        """Cast given object/data to pyds.NvDsInferTensorMeta, call
        pyds.NvDsInferTensorMeta.cast(data)
        """

    @typing.overload
    def cast(self: int) -> NvDsInferTensorMeta:
        """Cast given object/data to pyds.NvDsInferTensorMeta, call
        pyds.NvDsInferTensorMeta.cast(data)
        """

    def output_layers_info(self, arg0: int) -> NvDsInferLayerInfo:
        """Pointer to the array containing information for the bound output layers.
        Size of the array will be equal to num_output_layers. Pointers inside
        the NvDsInferLayerInfo structure are not valid for this array..
        """

    @property
    def gpu_id(self) -> int:
        """GPU device ID on which the device buffers have been allocated."""

    @property
    def num_output_layers(self) -> int:
        """Number of bound output layers."""

    @property
    def out_buf_ptrs_dev(self) -> typing.Any:
        """Array of pointers to the output device buffers for the frame / object.."""

    @property
    def out_buf_ptrs_host(self) -> typing.Any:
        """Array of pointers to the output host buffers for the frame / object."""

    @property
    def priv_data(self) -> typing.Any:
        """Private data used for the meta producer's internal memory management."""

    @property
    def unique_id(self) -> int:
        """Unique ID of the gst-nvinfer instance which attached this meta."""


class NvDsLabelInfo:
    """Holds information of label metadata in the classifier"""

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsLabelInfo]) -> NvDsLabelInfo:
        """Cast given object/data to pyds.NvDsLabelInfo, call
        pyds.NvDsLabelInfo.cast(data)
        """

    @typing.overload
    def cast(self: int) -> NvDsLabelInfo:
        """Cast given object/data to pyds.NvDsLabelInfo, call
        pyds.NvDsLabelInfo.cast(data)
        """

    @property
    def base_meta(self) -> NvDsBaseMeta:
        """base_meta"""

    @base_meta.setter
    def base_meta(self, arg0: NvDsBaseMeta) -> None: ...
    @property
    def label_id(self) -> int:
        """label_id in case of multi label classifier"""

    @label_id.setter
    def label_id(self, arg0: int) -> None: ...
    @property
    def num_classes(self) -> int:
        """Number of classes of the given label"""

    @num_classes.setter
    def num_classes(self, arg0: int) -> None: ...
    @property
    def pResult_label(self) -> str:
        """An object to store the result if it exceeds MAX_LABEL_SIZE bytes"""

    @pResult_label.setter
    def pResult_label(self, arg0: str) -> None: ...
    @property
    def result_class_id(self) -> int:
        """class_id of the best result"""

    @result_class_id.setter
    def result_class_id(self, arg0: int) -> None: ...
    @property
    def result_label(self) -> str:
        """An array to store the string describing the label of the classified object"""

    @result_label.setter
    def result_label(self, arg1: str) -> None: ...
    @property
    def result_prob(self) -> float:
        """Probability of best result"""

    @result_prob.setter
    def result_prob(self, arg0: float) -> None: ...


class NvDsMeta:
    """Holds DeepSteam meta data."""

    def __init__(self) -> None: ...
    @property
    def meta(self) -> Gst.Meta:
        """Meta"""

    @meta.setter
    def meta(self, arg0: Gst.Meta) -> None: ...
    @property
    def meta_data(self) -> typing.Any:
        """Must be cast to another structure based on @meta_type."""

    @meta_data.setter
    def meta_data(self, arg0: typing.Any) -> None: ...
    @property
    def meta_type(self) -> int:
        """meta_type"""

    @meta_type.setter
    def meta_type(self, arg0: int) -> None: ...
    @property
    def user_data(self) -> typing.Any:
        """user_data"""

    @user_data.setter
    def user_data(self, arg0: typing.Any) -> None: ...


NvDsMetaList: typing.TypeAlias = typing.Optional[GList[NvDsMeta]]


class NvDsMetaPool:
    """Holds information about given metadata pool."""

    def __init__(self) -> None: ...
    @property
    def element_size(self) -> int:
        """Size of an element in the given pool. Used for internal purpose"""

    @element_size.setter
    def element_size(self, arg0: int) -> None: ...
    @property
    def empty_list(self) -> NvDsMetaList:
        """List containing empty elements"""

    @empty_list.setter
    def empty_list(self, arg0: NvDsMetaList) -> None: ...
    @property
    def full_list(self) -> NvDsMetaList:
        """List containing full elements"""

    @full_list.setter
    def full_list(self, arg0: NvDsMetaList) -> None: ...
    @property
    def max_elements_in_pool(self) -> int:
        """Max elements in the pool. Used for internal purpose"""

    @max_elements_in_pool.setter
    def max_elements_in_pool(self, arg0: int) -> None: ...
    @property
    def meta_type(self) -> NvDsMetaType:
        """Type of the pool. Used for internal purpose"""

    @meta_type.setter
    def meta_type(self, arg0: NvDsMetaType) -> None: ...
    @property
    def num_empty_elements(self) -> int:
        """Number of empty elements. Used for internal purpose"""

    @num_empty_elements.setter
    def num_empty_elements(self, arg0: int) -> None: ...
    @property
    def num_full_elements(self) -> int:
        """Number of filled elements. These many elemnts are in use"""

    @num_full_elements.setter
    def num_full_elements(self, arg0: int) -> None: ...


class NvDsMetaType:
    """Specifies the type of meta data. NVIDIA defined NvDsMetaType will be present
                in the range from NVDS_BATCH_META to NVDS_START_USER_META.
                User can add it's own metadata type NVDS_START_USER_META onwards.


    Members:

      NVDS_INVALID_META : NVDS_INVALID_META

      NVDS_BATCH_META : metadata type to be set for formed batch

      NVDS_FRAME_META : metadata type to be set for frame

      NVDS_OBJ_META : metadata type to be set for detected object

      NVDS_DISPLAY_META : metadata type to be set for display

      NVDS_CLASSIFIER_META : metadata type to be set for object classifier

      NVDS_LABEL_INFO_META : metadata type to be set for given label of classifier

      NVDS_USER_META : used for internal purpose

      NVDS_PAYLOAD_META : metadata type to be set for payload generated by msg converter

      NVDS_EVENT_MSG_META : metadata type to be set for payload generated by msg broker

      NVDS_OPTICAL_FLOW_META : metadata type to be set for optical flow

      NVDS_LATENCY_MEASUREMENT_META : metadata type to be set for latency measurement

      NVDSINFER_TENSOR_OUTPUT_META : metadata type of raw inference output attached by
      gst-nvinfer. Refer NvDsInferTensorMeta for details.

      NVDSINFER_SEGMENTATION_META : metadata type of segmentation model output attached
      by gst-nvinfer. Refer NvDsInferSegmentationMeta for details.

      NVDS_CROP_IMAGE_META : Specifies metadata type for JPEG-encoded object crops.See
      the deepstream-image-meta-test app for details.

      NVDS_TRACKER_PAST_FRAME_META : metadata type to be set for tracking previous
      frames

      NVDS_AUDIO_BATCH_META : Specifies metadata type for formed audio batch.

      NVDS_AUDIO_FRAME_META : Specifies metadata type for audio frame.

      NVDS_RESERVED_META : Reserved field

      NVDS_GST_CUSTOM_META : metadata type to be set for metadata attached by nvidia
      gstreamer plugins before nvstreammux gstreamer plugin. It is set as user metadata
      inside @ref pyds.NvDsFrameMeta NVIDIA specific gst meta are in the range from
      NVDS_GST_CUSTOM_META to NVDS_GST_CUSTOM_META + 4096

      NVDS_START_USER_META : NVDS_START_USER_META

      NVDS_FORCE32_META : NVDS_FORCE32_META
    """

    NVDSINFER_SEGMENTATION_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDSINFER_SEGMENTATION_META
    NVDSINFER_TENSOR_OUTPUT_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDSINFER_TENSOR_OUTPUT_META
    NVDS_AUDIO_BATCH_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDS_AUDIO_BATCH_META
    NVDS_AUDIO_FRAME_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDS_AUDIO_FRAME_META
    NVDS_BATCH_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDS_BATCH_META
    NVDS_CLASSIFIER_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDS_CLASSIFIER_META
    NVDS_CROP_IMAGE_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDS_CROP_IMAGE_META
    NVDS_DISPLAY_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDS_DISPLAY_META
    NVDS_EVENT_MSG_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDS_EVENT_MSG_META
    NVDS_FORCE32_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDS_FORCE32_META
    NVDS_FRAME_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDS_FRAME_META
    NVDS_GST_CUSTOM_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDS_GST_CUSTOM_META
    NVDS_INVALID_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDS_INVALID_META
    NVDS_LABEL_INFO_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDS_LABEL_INFO_META
    NVDS_LATENCY_MEASUREMENT_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDS_LATENCY_MEASUREMENT_META
    NVDS_OBJ_META: typing.ClassVar[NvDsMetaType]  # value = NvDsMetaType.NVDS_OBJ_META
    NVDS_OPTICAL_FLOW_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDS_OPTICAL_FLOW_META
    NVDS_PAYLOAD_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDS_PAYLOAD_META
    NVDS_RESERVED_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDS_RESERVED_META
    NVDS_START_USER_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDS_START_USER_META
    NVDS_TRACKER_PAST_FRAME_META: typing.ClassVar[
        NvDsMetaType
    ]  # value = NvDsMetaType.NVDS_TRACKER_PAST_FRAME_META
    NVDS_USER_META: typing.ClassVar[NvDsMetaType]  # value = NvDsMetaType.NVDS_USER_META
    __members__: typing.ClassVar[
        dict[str, NvDsMetaType]
    ]  # value = {'NVDS_INVALID_META': NvDsMetaType.NVDS_INVALID_META,

    # 'NVDS_BATCH_META': NvDsMetaType.NVDS_BATCH_META,
    # 'NVDS_FRAME_META': NvDsMetaType.NVDS_FRAME_META,
    # 'NVDS_OBJ_META': NvDsMetaType.NVDS_OBJ_META,
    # 'NVDS_DISPLAY_META': NvDsMetaType.NVDS_DISPLAY_META,
    # 'NVDS_CLASSIFIER_META': NvDsMetaType.NVDS_CLASSIFIER_META,
    # 'NVDS_LABEL_INFO_META': NvDsMetaType.NVDS_LABEL_INFO_META,
    # 'NVDS_USER_META': NvDsMetaType.NVDS_USER_META,
    # 'NVDS_PAYLOAD_META': NvDsMetaType.NVDS_PAYLOAD_META,
    # 'NVDS_EVENT_MSG_META': NvDsMetaType.NVDS_EVENT_MSG_META,
    # 'NVDS_OPTICAL_FLOW_META': NvDsMetaType.NVDS_OPTICAL_FLOW_META,
    # 'NVDS_LATENCY_MEASUREMENT_META': NvDsMetaType.NVDS_LATENCY_MEASUREMENT_META,
    # 'NVDSINFER_TENSOR_OUTPUT_META': NvDsMetaType.NVDSINFER_TENSOR_OUTPUT_META,
    # 'NVDSINFER_SEGMENTATION_META': NvDsMetaType.NVDSINFER_SEGMENTATION_META,
    # 'NVDS_CROP_IMAGE_META': NvDsMetaType.NVDS_CROP_IMAGE_META,
    # 'NVDS_TRACKER_PAST_FRAME_META': NvDsMetaType.NVDS_TRACKER_PAST_FRAME_META,
    # 'NVDS_AUDIO_BATCH_META': NvDsMetaType.NVDS_AUDIO_BATCH_META,
    # 'NVDS_AUDIO_FRAME_META': NvDsMetaType.NVDS_AUDIO_FRAME_META,
    # 'NVDS_RESERVED_META': NvDsMetaType.NVDS_RESERVED_META,
    # 'NVDS_GST_CUSTOM_META': NvDsMetaType.NVDS_GST_CUSTOM_META,
    # 'NVDS_START_USER_META': NvDsMetaType.NVDS_START_USER_META,
    # 'NVDS_FORCE32_META': NvDsMetaType.NVDS_FORCE32_META}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str"""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvDsMetaType, arg0: int) -> None"""

    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...


class NvDsObjectMeta:
    """Holds information of object metadata in the frame"""

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsObjectMeta]) -> NvDsObjectMeta:
        """Cast given object/data to pyds.NvDsObjectMeta, call
        pyds.NvDsObjectMeta.cast(data)
        """

    @typing.overload
    def cast(self: int) -> NvDsObjectMeta:
        """Cast given object/data to pyds.NvDsObjectMeta, call
        pyds.NvDsObjectMeta.cast(data)
        """

    @property
    def base_meta(self) -> NvDsBaseMeta:
        """base_meta"""

    @base_meta.setter
    def base_meta(self, arg0: NvDsBaseMeta) -> None: ...
    @property
    def class_id(self) -> int:
        """Index of the object class infered by the primary detector/classifier"""

    @class_id.setter
    def class_id(self, arg0: int) -> None: ...
    @property
    def classifier_meta_list(self) -> typing.Optional[GList[NvDsClassifierMeta]]:
        """List of objects of type NvDsClassifierMeta"""

    @classifier_meta_list.setter
    def classifier_meta_list(
        self, arg0: typing.Optional[GList[NvDsClassifierMeta]]
    ) -> None: ...
    @property
    def confidence(self) -> float:
        """Confidence"""

    @confidence.setter
    def confidence(self, arg0: float) -> None: ...
    @property
    def detector_bbox_info(self) -> NvDsComp_BboxInfo:
        """Holds a structure containing bounding box parameters of the object when
        detected by detector.
        """

    @detector_bbox_info.setter
    def detector_bbox_info(self, arg0: NvDsComp_BboxInfo) -> None: ...
    @property
    def mask_params(self) -> typing.Any:
        """Holds mask parameters for the object. This mask is overlayed on object @see
        NvOSD_MaskParams.
        """

    @mask_params.setter
    def mask_params(self, arg0: typing.Any) -> None: ...
    @property
    def misc_obj_info(self) -> numpy.ndarray:
        """misc_obj_info"""

    @misc_obj_info.setter
    def misc_obj_info(self) -> None: ...
    @property
    def obj_label(self) -> str:
        """An array to store the string describing the class of the detected object"""

    @obj_label.setter
    def obj_label(self, arg1: str) -> None: ...
    @property
    def obj_user_meta_list(self) -> typing.Optional[GList[NvDsUserMeta]]:
        """List of objects of type NvDsUserMeta"""

    @obj_user_meta_list.setter
    def obj_user_meta_list(
        self, arg0: typing.Optional[GList[NvDsUserMeta]]
    ) -> None: ...
    @property
    def object_id(self) -> int:
        """Unique ID for tracking the object. @ref UNTRACKED_OBJECT_ID indicates the
        object has not been tracked
        """

    @object_id.setter
    def object_id(self, arg0: int) -> None: ...
    @property
    def parent(self) -> NvDsObjectMeta:
        """The parent pyds.NvDsObjectMeta object. Set to None if parent is not
        present
        """

    @parent.setter
    def parent(self, arg0: NvDsObjectMeta) -> None: ...
    @property
    def rect_params(self) -> NvOSD_RectParams:
        """Structure containing the positional parameters of the object in the frame.
        Can also be used to overlay borders / semi-transparent boxes on top of objects.
        Refer @see pyds.NvOSD_RectParams
        """

    @rect_params.setter
    def rect_params(self, arg0: NvOSD_RectParams) -> None: ...
    @property
    def reserved(self) -> numpy.ndarray:
        """Reserved"""

    @reserved.setter
    def reserved(self) -> None: ...
    @property
    def text_params(self) -> NvOSD_TextParams:
        """Text describing the object can be overlayed using this structure. @see
        pyds.NvOSD_TextParams
        """

    @text_params.setter
    def text_params(self, arg0: NvOSD_TextParams) -> None: ...
    @property
    def tracker_bbox_info(self) -> NvDsComp_BboxInfo:
        """Holds a structure containing bounding box coordinates of the object when
        processed by tracker.
        """

    @tracker_bbox_info.setter
    def tracker_bbox_info(self, arg0: NvDsComp_BboxInfo) -> None: ...
    @property
    def tracker_confidence(self) -> float:
        """Holds a confidence value for the object set by nvdcf_tracker.
        tracker_confidence will be set to -0.1 for KLT and IOU tracker
        """

    @tracker_confidence.setter
    def tracker_confidence(self, arg0: float) -> None: ...
    @property
    def unique_component_id(self) -> int:
        """Unique component id that attaches NvDsObjectMeta metadata"""

    @unique_component_id.setter
    def unique_component_id(self, arg0: int) -> None: ...


class NvDsObjectSignature:
    """Holds object signature."""

    def __init__(self) -> None: ...
    @property
    def signature(self) -> float:
        """Signature"""

    @signature.setter
    def signature(self, arg0: float) -> None: ...
    @property
    def size(self) -> int:
        """Size"""

    @size.setter
    def size(self, arg0: int) -> None: ...


class NvDsObjectType:
    """Object type flags.

    Members:

      NVDS_OBJECT_TYPE_VEHICLE :

      NVDS_OBJECT_TYPE_PERSON :

      NVDS_OBJECT_TYPE_FACE :

      NVDS_OBJECT_TYPE_BAG :

      NVDS_OBJECT_TYPE_BICYCLE :

      NVDS_OBJECT_TYPE_ROADSIGN :

      NVDS_OBJECT_TYPE_VEHICLE_EXT :

      NVDS_OBJECT_TYPE_PERSON_EXT :

      NVDS_OBJECT_TYPE_FACE_EXT :

      NVDS_OBJECT_TYPE_RESERVED : Reserved for future use. Use value greater than this
      for custom objects.

      NVDS_OBJECT_TYPE_CUSTOM : To support custom object.

      NVDS_OBJECT_TYPE_UNKNOWN :

      NVDS_OBEJCT_TYPE_FORCE32 :
    """

    NVDS_OBEJCT_TYPE_FORCE32: typing.ClassVar[
        NvDsObjectType
    ]  # value = NvDsObjectType.NVDS_OBEJCT_TYPE_FORCE32
    NVDS_OBJECT_TYPE_BAG: typing.ClassVar[
        NvDsObjectType
    ]  # value = NvDsObjectType.NVDS_OBJECT_TYPE_BAG
    NVDS_OBJECT_TYPE_BICYCLE: typing.ClassVar[
        NvDsObjectType
    ]  # value = NvDsObjectType.NVDS_OBJECT_TYPE_BICYCLE
    NVDS_OBJECT_TYPE_CUSTOM: typing.ClassVar[
        NvDsObjectType
    ]  # value = NvDsObjectType.NVDS_OBJECT_TYPE_CUSTOM
    NVDS_OBJECT_TYPE_FACE: typing.ClassVar[
        NvDsObjectType
    ]  # value = NvDsObjectType.NVDS_OBJECT_TYPE_FACE
    NVDS_OBJECT_TYPE_FACE_EXT: typing.ClassVar[
        NvDsObjectType
    ]  # value = NvDsObjectType.NVDS_OBJECT_TYPE_FACE_EXT
    NVDS_OBJECT_TYPE_PERSON: typing.ClassVar[
        NvDsObjectType
    ]  # value = NvDsObjectType.NVDS_OBJECT_TYPE_PERSON
    NVDS_OBJECT_TYPE_PERSON_EXT: typing.ClassVar[
        NvDsObjectType
    ]  # value = NvDsObjectType.NVDS_OBJECT_TYPE_PERSON_EXT
    NVDS_OBJECT_TYPE_RESERVED: typing.ClassVar[
        NvDsObjectType
    ]  # value = NvDsObjectType.NVDS_OBJECT_TYPE_RESERVED
    NVDS_OBJECT_TYPE_ROADSIGN: typing.ClassVar[
        NvDsObjectType
    ]  # value = NvDsObjectType.NVDS_OBJECT_TYPE_ROADSIGN
    NVDS_OBJECT_TYPE_UNKNOWN: typing.ClassVar[
        NvDsObjectType
    ]  # value = NvDsObjectType.NVDS_OBJECT_TYPE_UNKNOWN
    NVDS_OBJECT_TYPE_VEHICLE: typing.ClassVar[
        NvDsObjectType
    ]  # value = NvDsObjectType.NVDS_OBJECT_TYPE_VEHICLE
    NVDS_OBJECT_TYPE_VEHICLE_EXT: typing.ClassVar[
        NvDsObjectType
    ]  # value = NvDsObjectType.NVDS_OBJECT_TYPE_VEHICLE_EXT
    __members__: typing.ClassVar[
        dict[str, NvDsObjectType]
    ]  # value = {'NVDS_OBJECT_TYPE_VEHICLE': NvDsObjectType.NVDS_OBJECT_TYPE_VEHICLE,

    # 'NVDS_OBJECT_TYPE_PERSON': NvDsObjectType.NVDS_OBJECT_TYPE_PERSON,
    # 'NVDS_OBJECT_TYPE_FACE': NvDsObjectType.NVDS_OBJECT_TYPE_FACE,
    # 'NVDS_OBJECT_TYPE_BAG': NvDsObjectType.NVDS_OBJECT_TYPE_BAG,
    # 'NVDS_OBJECT_TYPE_BICYCLE': NvDsObjectType.NVDS_OBJECT_TYPE_BICYCLE,
    # 'NVDS_OBJECT_TYPE_ROADSIGN': NvDsObjectType.NVDS_OBJECT_TYPE_ROADSIGN,
    # 'NVDS_OBJECT_TYPE_VEHICLE_EXT': NvDsObjectType.NVDS_OBJECT_TYPE_VEHICLE_EXT,
    # 'NVDS_OBJECT_TYPE_PERSON_EXT': NvDsObjectType.NVDS_OBJECT_TYPE_PERSON_EXT,
    # 'NVDS_OBJECT_TYPE_FACE_EXT': NvDsObjectType.NVDS_OBJECT_TYPE_FACE_EXT,
    # 'NVDS_OBJECT_TYPE_RESERVED': NvDsObjectType.NVDS_OBJECT_TYPE_RESERVED,
    # 'NVDS_OBJECT_TYPE_CUSTOM': NvDsObjectType.NVDS_OBJECT_TYPE_CUSTOM,
    # 'NVDS_OBJECT_TYPE_UNKNOWN': NvDsObjectType.NVDS_OBJECT_TYPE_UNKNOWN,
    # 'NVDS_OBEJCT_TYPE_FORCE32': NvDsObjectType.NVDS_OBEJCT_TYPE_FORCE32}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str"""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvDsObjectType, arg0: int) -> None"""

    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...


class NvDsOpticalFlowMeta:
    """Holds information optical flow metadata information of a frame"""

    def cast(self: capsule[NvDsOpticalFlowMeta]) -> NvDsOpticalFlowMeta: ...
    @property
    def cols(self) -> int:
        """Number of columns present in the frame for given block size
        e.g. if block size is 4 and frame width is 1280, then
        number of columns = (1280 / 4) = 320
        """

    @cols.setter
    def cols(self, arg0: int) -> None: ...
    @property
    def data(self) -> typing.Any:
        """Motion vector data pointer"""

    @data.setter
    def data(self, arg0: typing.Any) -> None: ...
    @property
    def frame_num(self) -> int:
        """Current frame number of the source"""

    @frame_num.setter
    def frame_num(self, arg0: int) -> None: ...
    @property
    def mv_size(self) -> int:
        """Size of motion vector. Refer :class:`NvOFFlowVector`"""

    @mv_size.setter
    def mv_size(self, arg0: int) -> None: ...
    @property
    def priv(self) -> typing.Any:
        """Reserved field, for internal purpose only"""

    @priv.setter
    def priv(self, arg0: typing.Any) -> None: ...
    @property
    def reserved(self) -> typing.Any:
        """Reserved field, for internal purpose only"""

    @reserved.setter
    def reserved(self, arg0: typing.Any) -> None: ...
    @property
    def rows(self) -> int:
        """Number of rows present in the frame for given block size
        e.g. if block size is 4 and frame height is 720, then
        number of rows = (720 / 4) = 180
        """

    @rows.setter
    def rows(self, arg0: int) -> None: ...


class NvDsPastFrameObj:
    """NvDsPastFrameObj"""

    def __init__(self) -> None: ...
    def cast(self: capsule[NvDsPastFrameObj]) -> NvDsPastFrameObj:
        """Cast to NvDsPastFrameObjDoc"""

    @property
    def age(self) -> int:
        """Age"""

    @age.setter
    def age(self, arg0: int) -> None: ...
    @property
    def confidence(self) -> float:
        """Confidence"""

    @confidence.setter
    def confidence(self, arg0: float) -> None: ...
    @property
    def frameNum(self) -> int:
        """FrameNum"""

    @frameNum.setter
    def frameNum(self, arg0: int) -> None: ...
    @property
    def tBbox(self) -> NvOSD_RectParams:
        """TBbox"""

    @tBbox.setter
    def tBbox(self, arg0: NvOSD_RectParams) -> None: ...


class NvDsPastFrameObjBatch:
    """Batch of lists of buffered objects"""

    def __init__(self) -> None: ...
    def cast(self: capsule[NvDsPastFrameObjBatch]) -> NvDsPastFrameObjBatch:
        """Cast to NvDsPastFrameObjBatchDoc"""

    def list(self) -> typing.Iterator:
        """Pointer to array of stream lists."""

    @property
    def numAllocated(self) -> int:
        """Number of blocks allocated for the list."""

    @numAllocated.setter
    def numAllocated(self, arg0: int) -> None: ...
    @property
    def numFilled(self) -> int:
        """Number of filled blocks in the list."""

    @numFilled.setter
    def numFilled(self, arg0: int) -> None: ...


class NvDsPastFrameObjList:
    """One object in several past frames"""

    def __init__(self) -> None: ...
    def cast(self: capsule[NvDsPastFrameObjList]) -> NvDsPastFrameObjList:
        """Cast to NvDsPastFrameObjListDoc"""

    def list(self) -> typing.Iterator:
        """Pointer to past frame info of this object."""

    @property
    def classId(self) -> int:
        """Object class id."""

    @classId.setter
    def classId(self, arg0: int) -> None: ...
    @property
    def numObj(self) -> int:
        """Number of frames this object appreared in the past."""

    @numObj.setter
    def numObj(self, arg0: int) -> None: ...
    @property
    def objLabel(self) -> str:
        """An array of the string describing the object class."""

    @objLabel.setter
    def objLabel(self, arg1: str) -> None: ...
    @property
    def uniqueId(self) -> int:
        """Object tracking id."""

    @uniqueId.setter
    def uniqueId(self, arg0: int) -> None: ...


class NvDsPastFrameObjStream:
    """List of objects in each stream."""

    def __init__(self) -> None: ...
    def cast(self: capsule[NvDsPastFrameObjStream]) -> NvDsPastFrameObjStream:
        """Cast to NvDsPastFrameObjStreamDoc"""

    def list(self) -> typing.Iterator:
        """Pointer to objects inside this stream."""

    @property
    def numAllocated(self) -> int:
        """Maximum number of objects allocated."""

    @numAllocated.setter
    def numAllocated(self, arg0: int) -> None: ...
    @property
    def numFilled(self) -> int:
        """Number of objects in this frame."""

    @numFilled.setter
    def numFilled(self, arg0: int) -> None: ...
    @property
    def streamID(self) -> int:
        """Stream id the same as frame_meta->pad_index."""

    @streamID.setter
    def streamID(self, arg0: int) -> None: ...
    @property
    def surfaceStreamID(self) -> int:
        """Stream id used inside tracker plugin."""

    @surfaceStreamID.setter
    def surfaceStreamID(self, arg0: int) -> None: ...


class NvDsPayload:
    """Holds payload meta data."""

    def __init__(self) -> None: ...
    @property
    def componentId(self) -> int:
        """Id of component who attached the payload (Optional)"""

    @componentId.setter
    def componentId(self, arg0: int) -> None: ...
    @property
    def payload(self) -> typing.Any:
        """Payload object"""

    @payload.setter
    def payload(self, arg0: typing.Any) -> None: ...
    @property
    def payloadSize(self) -> int:
        """Size of payload"""

    @payloadSize.setter
    def payloadSize(self, arg0: int) -> None: ...


class NvDsPayloadType:
    """Payload type flags.

    Members:

      NVDS_PAYLOAD_DEEPSTREAM :

      NVDS_PAYLOAD_DEEPSTREAM_MINIMAL :

      NVDS_PAYLOAD_RESERVED : Reserved for future use. Use value greater than this for
      custom payloads.

      NVDS_PAYLOAD_CUSTOM : To support custom payload. User need to implement
      nvds_msg2p_* interface

      NVDS_PAYLOAD_FORCE32 :
    """

    NVDS_PAYLOAD_CUSTOM: typing.ClassVar[
        NvDsPayloadType
    ]  # value = NvDsPayloadType.NVDS_PAYLOAD_CUSTOM
    NVDS_PAYLOAD_DEEPSTREAM: typing.ClassVar[
        NvDsPayloadType
    ]  # value = NvDsPayloadType.NVDS_PAYLOAD_DEEPSTREAM
    NVDS_PAYLOAD_DEEPSTREAM_MINIMAL: typing.ClassVar[
        NvDsPayloadType
    ]  # value = NvDsPayloadType.NVDS_PAYLOAD_DEEPSTREAM_MINIMAL
    NVDS_PAYLOAD_FORCE32: typing.ClassVar[
        NvDsPayloadType
    ]  # value = NvDsPayloadType.NVDS_PAYLOAD_FORCE32
    NVDS_PAYLOAD_RESERVED: typing.ClassVar[
        NvDsPayloadType
    ]  # value = NvDsPayloadType.NVDS_PAYLOAD_RESERVED
    __members__: typing.ClassVar[
        dict[str, NvDsPayloadType]
    ]  # value = {'NVDS_PAYLOAD_DEEPSTREAM': NvDsPayloadType.NVDS_PAYLOAD_DEEPSTREAM,

    # 'NVDS_PAYLOAD_DEEPSTREAM_MINIMAL':
    # NvDsPayloadType.NVDS_PAYLOAD_DEEPSTREAM_MINIMAL,
    # 'NVDS_PAYLOAD_RESERVED': NvDsPayloadType.NVDS_PAYLOAD_RESERVED,
    # 'NVDS_PAYLOAD_CUSTOM': NvDsPayloadType.NVDS_PAYLOAD_CUSTOM,
    # 'NVDS_PAYLOAD_FORCE32': NvDsPayloadType.NVDS_PAYLOAD_FORCE32}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str"""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvDsPayloadType, arg0: int) -> None"""

    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...


class NvDsPersonObject:
    """Holds person object parameters."""

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsPersonObject]) -> NvDsPersonObject:
        """Casts to Person object, call pyds.NvDsPersonObject(data)"""

    @typing.overload
    def cast(self: int) -> NvDsPersonObject:
        """Casts to Person object, call pyds.NvDsPersonObject(data)"""

    @property
    def age(self) -> int:
        """Age"""

    @age.setter
    def age(self, arg0: int) -> None: ...
    @property
    def apparel(self) -> int:
        """Apparel"""

    @apparel.setter
    def apparel(self, arg1: str) -> None: ...
    @property
    def cap(self) -> int:
        """Cap"""

    @cap.setter
    def cap(self, arg1: str) -> None: ...
    @property
    def gender(self) -> int:
        """Gender"""

    @gender.setter
    def gender(self, arg1: str) -> None: ...
    @property
    def hair(self) -> int:
        """Hair"""

    @hair.setter
    def hair(self, arg1: str) -> None: ...


class NvDsPersonObjectExt:
    """Holds a vehicle object's parameters."""

    def __init__(self) -> None: ...
    @property
    def age(self) -> int:
        """Object holding information of person's age."""

    @age.setter
    def age(self, arg0: int) -> None: ...
    @property
    def apparel(self) -> str:
        """Object holding description of the person's apparel."""

    @apparel.setter
    def apparel(self, arg0: str) -> None: ...
    @property
    def cap(self) -> str:
        """Object holding information of the type of cap person is wearing."""

    @cap.setter
    def cap(self, arg0: str) -> None: ...
    @property
    def gender(self) -> str:
        """Object holding information of person's gender."""

    @gender.setter
    def gender(self, arg0: str) -> None: ...
    @property
    def hair(self) -> str:
        """Object holding information of person's hair color."""

    @hair.setter
    def hair(self, arg0: str) -> None: ...
    @property
    def mask(self) -> typing.Optional[GList[typing.Any]]:
        """List of polygons for person mask."""

    @mask.setter
    def mask(self, arg0: typing.Optional[GList[typing.Any]]) -> None: ...


class NvDsRect:
    """Holds rectangle parameters."""

    def __init__(self) -> None: ...
    @property
    def height(self) -> float:
        """Height"""

    @height.setter
    def height(self, arg0: float) -> None: ...
    @property
    def left(self) -> float:
        """Left"""

    @left.setter
    def left(self, arg0: float) -> None: ...
    @property
    def top(self) -> float:
        """Top"""

    @top.setter
    def top(self, arg0: float) -> None: ...
    @property
    def width(self) -> float:
        """Width"""

    @width.setter
    def width(self, arg0: float) -> None: ...


class NvDsUserMeta:
    """Holds information of user metadata that user can specify"""

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsUserMeta]) -> NvDsUserMeta:
        """Cast given object/data to pyds.NvDsUserMeta, call
        pyds.NvDsUserMeta.cast(data)
        """

    @typing.overload
    def cast(self: int) -> NvDsUserMeta:
        """Cast given object/data to pyds.NvDsUserMeta, call
        pyds.NvDsUserMeta.cast(data)
        """

    @property
    def base_meta(self) -> NvDsBaseMeta:
        """base_meta"""

    @base_meta.setter
    def base_meta(self, arg0: NvDsBaseMeta) -> None: ...
    @property
    def user_meta_data(self) -> typing.Any:
        """User data object to be attached Refer to deepstream-user-metadata-test
        example for usage
        """

    @user_meta_data.setter
    def user_meta_data(self, arg0: typing.Any) -> None: ...


class NvDsVehicleObject:
    """Holds vehicle object parameters."""

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsVehicleObject]) -> NvDsVehicleObject:
        """Casts to Vehicle object, call pyds.NvDsVehicleObject(data)"""

    @typing.overload
    def cast(self: int) -> NvDsVehicleObject:
        """Casts to Vehicle object, call pyds.NvDsVehicleObject(data)"""

    @property
    def color(self) -> int:
        """Color"""

    @color.setter
    def color(self, arg1: str) -> None: ...
    @property
    def license(self) -> int:
        """License"""

    @license.setter
    def license(self, arg1: str) -> None: ...
    @property
    def make(self) -> int:
        """Make"""

    @make.setter
    def make(self, arg1: str) -> None: ...
    @property
    def model(self) -> int:
        """Model"""

    @model.setter
    def model(self, arg1: str) -> None: ...
    @property
    def region(self) -> int:
        """Region"""

    @region.setter
    def region(self, arg1: str) -> None: ...
    @property
    def type(self) -> int:
        """Type"""

    @type.setter
    def type(self, arg1: str) -> None: ...


class NvDsVehicleObjectExt:
    """Holds a vehicle object's parameters."""

    def __init__(self) -> None: ...
    @property
    def color(self) -> str:
        """Object holding information of vehicle color."""

    @color.setter
    def color(self, arg0: str) -> None: ...
    @property
    def license(self) -> str:
        """Object holding information of the licesnse number."""

    @license.setter
    def license(self, arg0: str) -> None: ...
    @property
    def make(self) -> str:
        """Object holding information of vehicle make."""

    @make.setter
    def make(self, arg0: str) -> None: ...
    @property
    def mask(self) -> typing.Optional[GList[typing.Any]]:
        """List of polygons for vehicle mask."""

    @mask.setter
    def mask(self, arg0: typing.Optional[GList[typing.Any]]) -> None: ...
    @property
    def model(self) -> str:
        """Object holding information of vehicle model."""

    @model.setter
    def model(self, arg0: str) -> None: ...
    @property
    def region(self) -> str:
        """Object holding information of region of the vehicle."""

    @region.setter
    def region(self, arg0: str) -> None: ...
    @property
    def type(self) -> str:
        """Object holding information of vehicle type."""

    @type.setter
    def type(self, arg0: str) -> None: ...


class NvOFFlowVector:
    """Holds information about motion vector information of an element."""

    @property
    def flowx(self) -> int:
        """X component of motion vector"""

    @flowx.setter
    def flowx(self, arg0: int) -> None: ...
    @property
    def flowy(self) -> int:
        """Y component of motion vector"""

    @flowy.setter
    def flowy(self, arg0: int) -> None: ...


class NvOSD_ArrowParams:
    """ """

    def __init__(self) -> None: ...
    @property
    def arrow_color(self) -> NvOSD_ColorParams:
        """Holds color params of the arrow box."""

    @arrow_color.setter
    def arrow_color(self, arg0: NvOSD_ColorParams) -> None: ...
    @property
    def arrow_head(self) -> NvOSD_Arrow_Head_Direction:
        """Holds arrow_head position."""

    @arrow_head.setter
    def arrow_head(self, arg0: NvOSD_Arrow_Head_Direction) -> None: ...
    @property
    def arrow_width(self) -> int:
        """Holds arrow_width in pixels."""

    @arrow_width.setter
    def arrow_width(self, arg0: int) -> None: ...
    @property
    def x1(self) -> int:
        """Holds start horizontal coordinate in pixels."""

    @x1.setter
    def x1(self, arg0: int) -> None: ...
    @property
    def x2(self) -> int:
        """Holds end horizontal coordinate in pixels."""

    @x2.setter
    def x2(self, arg0: int) -> None: ...
    @property
    def y1(self) -> int:
        """Holds start vertical coordinate in pixels."""

    @y1.setter
    def y1(self, arg0: int) -> None: ...
    @property
    def y2(self) -> int:
        """Holds end vertical coordinate in pixels."""

    @y2.setter
    def y2(self, arg0: int) -> None: ...


class NvOSD_Arrow_Head_Direction:
    """Lists arrow head positions.

    Members:

      START_HEAD :
                Arrow head only at start = 0.


      END_HEAD :
                Arrow head only at end = 1.


      BOTH_HEAD :
                Arrow head at both sides = 2.

    """

    BOTH_HEAD: typing.ClassVar[
        NvOSD_Arrow_Head_Direction
    ]  # value = NvOSD_Arrow_Head_Direction.BOTH_HEAD
    END_HEAD: typing.ClassVar[
        NvOSD_Arrow_Head_Direction
    ]  # value = NvOSD_Arrow_Head_Direction.END_HEAD
    START_HEAD: typing.ClassVar[
        NvOSD_Arrow_Head_Direction
    ]  # value = NvOSD_Arrow_Head_Direction.START_HEAD
    __members__: typing.ClassVar[
        dict[str, NvOSD_Arrow_Head_Direction]
    ]  # value = {'START_HEAD': NvOSD_Arrow_Head_Direction.START_HEAD, 'END_HEAD':

    # NvOSD_Arrow_Head_Direction.END_HEAD, 'BOTH_HEAD':
    # NvOSD_Arrow_Head_Direction.BOTH_HEAD}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str"""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvOSD_Arrow_Head_Direction, arg0: int) -> None"""

    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...


class NvOSD_CircleParams:
    """Holds the circle parameters to be overlayed."""

    def __init__(self) -> None: ...
    @property
    def bg_color(self) -> NvOSD_ColorParams:
        """Holds the circle parameters to be overlayed."""

    @bg_color.setter
    def bg_color(self, arg0: NvOSD_ColorParams) -> None: ...
    @property
    def circle_color(self) -> NvOSD_ColorParams:
        """Holds color params of the arrow box.."""

    @circle_color.setter
    def circle_color(self, arg0: NvOSD_ColorParams) -> None: ...
    @property
    def has_bg_color(self) -> int:
        """Holds boolean value indicating whether
        circle has background color..
        """

    @has_bg_color.setter
    def has_bg_color(self, arg0: int) -> None: ...
    @property
    def radius(self) -> int:
        """Holds radius of circle in pixels."""

    @radius.setter
    def radius(self, arg0: int) -> None: ...
    @property
    def reserved(self) -> int:
        """Reserved field for future usage.
        For internal purpose only..
        """

    @reserved.setter
    def reserved(self, arg0: int) -> None: ...
    @property
    def xc(self) -> int:
        """Holds start horizontal coordinate in pixels."""

    @xc.setter
    def xc(self, arg0: int) -> None: ...
    @property
    def yc(self) -> int:
        """Holds start vertical coordinate in pixels."""

    @yc.setter
    def yc(self, arg0: int) -> None: ...


class NvOSD_ColorParams:
    """Holds the color parameters of the box or text to be overlayed."""

    def __init__(self) -> None: ...
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None:
        """Sets the color values"""

    @property
    def alpha(self) -> float:
        """Holds alpha component of color. Value must be in the range 0-1."""

    @alpha.setter
    def alpha(self, arg0: float) -> None: ...
    @property
    def blue(self) -> float:
        """Holds blue component of color. Value must be in the range 0-1."""

    @blue.setter
    def blue(self, arg0: float) -> None: ...
    @property
    def green(self) -> float:
        """Holds green component of color. Value must be in the range 0-1."""

    @green.setter
    def green(self, arg0: float) -> None: ...
    @property
    def red(self) -> float:
        """Holds red component of color. Value must be in the range 0-1."""

    @red.setter
    def red(self, arg0: float) -> None: ...


class NvOSD_Color_info:
    def __init__(self) -> None: ...
    @property
    def color(self) -> NvOSD_ColorParams:
        """Color"""

    @color.setter
    def color(self, arg0: NvOSD_ColorParams) -> None: ...
    @property
    def id(self) -> int:
        """Id"""

    @id.setter
    def id(self, arg0: int) -> None: ...


class NvOSD_FontParams:
    """Holds the font parameters of the text to be overlayed."""

    def __init__(self) -> None: ...
    @property
    def font_color(self) -> NvOSD_ColorParams:
        """Holds pointer to the string containing
        font name. The list of supported fonts
        can be obtained by running fc-list
        command
        """

    @font_color.setter
    def font_color(self, arg0: NvOSD_ColorParams) -> None: ...
    @property
    def font_name(self) -> int:
        """Holds pointer to the string containing
        font name. The list of supported fonts
        can be obtained by running fc-list
        command
        """

    @font_name.setter
    def font_name(self, arg1: str) -> None: ...
    @property
    def font_size(self) -> int:
        """Holds size of the font."""

    @font_size.setter
    def font_size(self, arg0: int) -> None: ...


class NvOSD_FrameArrowParams:
    """Holds Frame Arrow Params"""

    def __init__(self) -> None: ...
    @property
    def arrow_params_list(self) -> NvOSD_ArrowParams:
        """Holds params of arrows."""

    @arrow_params_list.setter
    def arrow_params_list(self, arg0: NvOSD_ArrowParams) -> None: ...
    @property
    def buf_ptr(self) -> NvBufSurfaceParams:
        """Holds pointer to the buffer containing frame."""

    @buf_ptr.setter
    def buf_ptr(self, arg0: NvBufSurfaceParams) -> None: ...
    @property
    def mode(self) -> NvOSD_Mode:
        """Holds OSD Mode to be used for processing."""

    @mode.setter
    def mode(self, arg0: NvOSD_Mode) -> None: ...
    @property
    def num_arrows(self) -> int:
        """Holds number of arrows."""

    @num_arrows.setter
    def num_arrows(self, arg0: int) -> None: ...


class NvOSD_FrameCircleParams:
    """Holds Frame Circle Params"""

    def __init__(self) -> None: ...
    @property
    def buf_ptr(self) -> NvBufSurfaceParams:
        """Holds pointer to the buffer containing frame."""

    @buf_ptr.setter
    def buf_ptr(self, arg0: NvBufSurfaceParams) -> None: ...
    @property
    def circle_params_list(self) -> NvOSD_CircleParams:
        """Holds params of circles."""

    @circle_params_list.setter
    def circle_params_list(self, arg0: NvOSD_CircleParams) -> None: ...
    @property
    def mode(self) -> NvOSD_Mode:
        """Holds OSD Mode to be used for processing."""

    @mode.setter
    def mode(self, arg0: NvOSD_Mode) -> None: ...
    @property
    def num_circles(self) -> int:
        """Holds number of circles."""

    @num_circles.setter
    def num_circles(self, arg0: int) -> None: ...


class NvOSD_FrameLineParams:
    """Holds Frame Line Params"""

    def __init__(self) -> None: ...
    @property
    def buf_ptr(self) -> NvBufSurfaceParams:
        """Holds pointer to the buffer containing frame."""

    @buf_ptr.setter
    def buf_ptr(self, arg0: NvBufSurfaceParams) -> None: ...
    @property
    def line_params_list(self) -> NvOSD_LineParams:
        """Holds params of lines."""

    @line_params_list.setter
    def line_params_list(self, arg0: NvOSD_LineParams) -> None: ...
    @property
    def mode(self) -> NvOSD_Mode:
        """Holds OSD Mode to be used for processing."""

    @mode.setter
    def mode(self, arg0: NvOSD_Mode) -> None: ...
    @property
    def num_lines(self) -> int:
        """Holds number of lines."""

    @num_lines.setter
    def num_lines(self, arg0: int) -> None: ...


class NvOSD_FrameRectParams:
    """Holds Frame Rect Params"""

    def __init__(self) -> None: ...
    @property
    def buf_ptr(self) -> NvBufSurfaceParams:
        """Holds pointer to the buffer containing frame."""

    @buf_ptr.setter
    def buf_ptr(self, arg0: NvBufSurfaceParams) -> None: ...
    @property
    def mode(self) -> NvOSD_Mode:
        """Holds OSD Mode to be used for processing."""

    @mode.setter
    def mode(self, arg0: NvOSD_Mode) -> None: ...
    @property
    def num_rects(self) -> int:
        """Holds number of Rectangles."""

    @num_rects.setter
    def num_rects(self, arg0: int) -> None: ...
    @property
    def rect_params_list(self) -> NvOSD_RectParams:
        """Holds params of Rectangles."""

    @rect_params_list.setter
    def rect_params_list(self, arg0: NvOSD_RectParams) -> None: ...


class NvOSD_FrameTextParams:
    """Holds Frame Text parameters."""

    def __init__(self) -> None: ...
    @property
    def buf_ptr(self) -> NvBufSurfaceParams:
        """Holds pointer to the buffer containing frame."""

    @buf_ptr.setter
    def buf_ptr(self, arg0: NvBufSurfaceParams) -> None: ...
    @property
    def mode(self) -> NvOSD_Mode:
        """Holds OSD Mode to be used for processing."""

    @mode.setter
    def mode(self, arg0: NvOSD_Mode) -> None: ...
    @property
    def num_strings(self) -> int:
        """Holds number of strings."""

    @num_strings.setter
    def num_strings(self, arg0: int) -> None: ...
    @property
    def text_params_list(self) -> NvOSD_TextParams:
        """Holds text params of string."""

    @text_params_list.setter
    def text_params_list(self, arg0: NvOSD_TextParams) -> None: ...


class NvOSD_LineParams:
    """Holds the box parameters of the line to be overlayed."""

    def __init__(self) -> None: ...
    @property
    def line_color(self) -> NvOSD_ColorParams:
        """Holds color params of the border of the box."""

    @line_color.setter
    def line_color(self, arg0: NvOSD_ColorParams) -> None: ...
    @property
    def line_width(self) -> int:
        """Holds border_width of the box in pixels."""

    @line_width.setter
    def line_width(self, arg0: int) -> None: ...
    @property
    def x1(self) -> int:
        """Holds left coordinate of the box in pixels."""

    @x1.setter
    def x1(self, arg0: int) -> None: ...
    @property
    def x2(self) -> int:
        """Holds width of the box in pixels."""

    @x2.setter
    def x2(self, arg0: int) -> None: ...
    @property
    def y1(self) -> int:
        """Holds top coordinate of the box in pixels."""

    @y1.setter
    def y1(self, arg0: int) -> None: ...
    @property
    def y2(self) -> int:
        """Holds height of the box in pixels."""

    @y2.setter
    def y2(self, arg0: int) -> None: ...


class NvOSD_Mode:
    """List modes used to overlay boxes and text

    Members:

      MODE_CPU :
                     Selects CPU for OSD processing.
                    Works with RGBA data only


      MODE_GPU :
                     Selects GPU for OSD processing.
                    Yet to be implemented


      MODE_HW :
                     Selects NV HW engine for rectangle draw and mask.
                       This mode works with both YUV and RGB data.
                       It does not consider alpha parameter.
                       Not applicable for drawing text.

    """

    MODE_CPU: typing.ClassVar[NvOSD_Mode]  # value = NvOSD_Mode.MODE_CPU
    MODE_GPU: typing.ClassVar[NvOSD_Mode]  # value = NvOSD_Mode.MODE_GPU
    MODE_HW: typing.ClassVar[NvOSD_Mode]  # value = NvOSD_Mode.MODE_HW
    __members__: typing.ClassVar[
        dict[str, NvOSD_Mode]
    ]  # value = {'MODE_CPU': NvOSD_Mode.MODE_CPU, 'MODE_GPU': NvOSD_Mode.MODE_GPU,

    # 'MODE_HW': NvOSD_Mode.MODE_HW}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str"""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvOSD_Mode, arg0: int) -> None"""

    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...


class NvOSD_RectParams:
    """Holds the box parameters of the box to be overlayed."""

    def __init__(self) -> None: ...
    @property
    def bg_color(self) -> NvOSD_ColorParams:
        """Holds background color of the box."""

    @bg_color.setter
    def bg_color(self, arg0: NvOSD_ColorParams) -> None: ...
    @property
    def border_color(self) -> NvOSD_ColorParams:
        """Holds color params of the border of the box."""

    @border_color.setter
    def border_color(self, arg0: NvOSD_ColorParams) -> None: ...
    @property
    def border_width(self) -> int:
        """Holds border_width of the box in pixels."""

    @border_width.setter
    def border_width(self, arg0: int) -> None: ...
    @property
    def color_id(self) -> int:
        """Id of the color"""

    @color_id.setter
    def color_id(self, arg0: int) -> None: ...
    @property
    def has_bg_color(self) -> int:
        """Holds boolean value indicating whether box
        has background color.
        """

    @has_bg_color.setter
    def has_bg_color(self, arg0: int) -> None: ...
    @property
    def has_color_info(self) -> int:
        """color_info"""

    @has_color_info.setter
    def has_color_info(self, arg0: int) -> None: ...
    @property
    def height(self) -> float:
        """Holds height of the box in pixels."""

    @height.setter
    def height(self, arg0: float) -> None: ...
    @property
    def left(self) -> float:
        """Holds left coordinate of the box in pixels."""

    @left.setter
    def left(self, arg0: float) -> None: ...
    @property
    def reserved(self) -> int:
        """Reserved field for future usage.
        For internal purpose only
        """

    @reserved.setter
    def reserved(self, arg0: int) -> None: ...
    @property
    def top(self) -> float:
        """Holds top coordinate of the box in pixels."""

    @top.setter
    def top(self, arg0: float) -> None: ...
    @property
    def width(self) -> float:
        """Holds width of the box in pixels."""

    @width.setter
    def width(self, arg0: float) -> None: ...


class NvOSD_TextParams:
    """Holds the text parameters of the text to be overlayed"""

    def __init__(self) -> None: ...
    @property
    def display_text(self) -> int:
        """Holds the text to be overlayed"""

    @display_text.setter
    def display_text(self, arg1: str) -> None: ...
    @property
    def font_params(self) -> NvOSD_FontParams:
        """font_params."""

    @font_params.setter
    def font_params(self, arg0: NvOSD_FontParams) -> None: ...
    @property
    def set_bg_clr(self) -> int:
        """Boolean to indicate text has background color."""

    @set_bg_clr.setter
    def set_bg_clr(self, arg0: int) -> None: ...
    @property
    def text_bg_clr(self) -> NvOSD_ColorParams:
        """Background color for text."""

    @text_bg_clr.setter
    def text_bg_clr(self, arg0: NvOSD_ColorParams) -> None: ...
    @property
    def x_offset(self) -> int:
        """Holds horizontal offset w.r.t top left pixel of the frame."""

    @x_offset.setter
    def x_offset(self, arg0: int) -> None: ...
    @property
    def y_offset(self) -> int:
        """Holds vertical offset w.r.t top left pixel of   the frame."""

    @y_offset.setter
    def y_offset(self, arg0: int) -> None: ...


class ROI_STATUS_360D:
    """Defines DeepStream 360d metadata.

    Members:

      ROI_ENTRY_360D : ROI_ENTRY_360D

      ROI_EXIT_360D : ROI_EXIT_360D.

      INSIDE_AISLE_360D : INSIDE_AISLE_360D.
    """

    INSIDE_AISLE_360D: typing.ClassVar[
        ROI_STATUS_360D
    ]  # value = ROI_STATUS_360D.INSIDE_AISLE_360D
    ROI_ENTRY_360D: typing.ClassVar[
        ROI_STATUS_360D
    ]  # value = ROI_STATUS_360D.ROI_ENTRY_360D
    ROI_EXIT_360D: typing.ClassVar[
        ROI_STATUS_360D
    ]  # value = ROI_STATUS_360D.ROI_EXIT_360D
    __members__: typing.ClassVar[
        dict[str, ROI_STATUS_360D]
    ]  # value = {'ROI_ENTRY_360D': ROI_STATUS_360D.ROI_ENTRY_360D,

    # 'ROI_EXIT_360D': ROI_STATUS_360D.ROI_EXIT_360D,
    # 'INSIDE_AISLE_360D': ROI_STATUS_360D.INSIDE_AISLE_360D}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_"""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool"""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str"""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.ROI_STATUS_360D, arg0: int) -> None"""

    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...


class RectDim:
    """RectDim"""

    def __init__(self) -> None: ...
    @property
    def class_id(self) -> int:
        """class_id"""

    @class_id.setter
    def class_id(self, arg0: int) -> None: ...
    @property
    def gie_unique_id(self) -> int:
        """gie_unique_id"""

    @gie_unique_id.setter
    def gie_unique_id(self, arg0: int) -> None: ...
    @property
    def height(self) -> float:
        """Height"""

    @height.setter
    def height(self, arg0: float) -> None: ...
    @property
    def left(self) -> float:
        """Left"""

    @left.setter
    def left(self, arg0: float) -> None: ...
    @property
    def roi_status(self) -> int:
        """roi_status"""

    @roi_status.setter
    def roi_status(self, arg0: int) -> None: ...
    @property
    def text(self) -> typing.Any:
        """Text"""

    @text.setter
    def text(self, arg0: typing.Any) -> None: ...
    @property
    def top(self) -> float:
        """Top"""

    @top.setter
    def top(self, arg0: float) -> None: ...
    @property
    def tracking_id(self) -> int:
        """tracking_id"""

    @tracking_id.setter
    def tracking_id(self, arg0: int) -> None: ...
    @property
    def width(self) -> float:
        """Width"""

    @width.setter
    def width(self, arg0: float) -> None: ...


def NvBufSurfaceCopy(srcSurf: NvBufSurface, dstSurf: NvBufSurface) -> int:
    """Copy the memory content of source batched buffer(s) to memory of destination
    batched buffer(s).

    This function can be used to copy source buffer(s) of one memory type
    to destination buffer(s) of different memory type.
    e.g. CUDA Host to CUDA Device or malloced memory to CUDA device etc.

    Both source and destination NvBufSurface must have same buffer and batch size.

    :arg srcSurf: pointer to source NvBufSurface structure.
    :arg dstSurf: pointer to destination NvBufSurface structure.

    returns: 0 for success, -1 for failure.
    """


def NvBufSurfaceCreate(
    surf: NvBufSurface, batchSize: int, params: NvBufSurfaceCreateParams
) -> int:
    """Allocate batch of buffers.

    Allocates memory for batchSize buffers and returns in surf object  allocated
    NvBufSurface.
    params object should have allocation parameters of single object. If size field in
    params is set, buffer of that size will be allocated and all other
    parameters (w, h, color format etc.) will be ignored.

    Use NvBufSurfaceDestroy to free all the resources.

    :arg surf: pointer to allocated batched buffers.
    :arg batchSize: batch size of buffers.
    :arg params: pointer to NvBufSurfaceCreateParams structure.

    :returns: 0 for success, -1 for failure.
    """


def NvBufSurfaceDestroy(surf: NvBufSurface) -> int:
    """Free the batched buffers previously allocated through NvBufSurfaceCreate.

    :arg surf: An object to NvBufSurface to free.

    :returns: 0 for success, -1 for failure.
    """


def NvBufSurfaceFromFd(dmabuf_fd: int, buffer: capsule[NvBufSurface]) -> int:
    """Get the NvBufSurface from the dmabuf fd.

    :arg dmabuf_fd: dmabuf fd of the buffer.
    :arg buffer: pointer to NvBufSurface.

    :returns: 0 for success, -1 for failure.
    """


def NvBufSurfaceMap(
    surf: NvBufSurface, index: int, plane: int, type: NvBufSurfaceMemMapFlags
) -> int:
    """Map HW batched buffers to HOST CPU address space.

     Valid for NVBUF_MEM_CUDA_UNIFIED type of memory for dGPU and
    NVBUF_MEM_SURFACE_ARRAY and NVBUF_MEM_HANDLE type of memory for Jetson.

    This function will fill addr array of NvBufSurfaceMappedAddr field of
    NvBufSurfaceParams
    with the CPU mapped memory pointers.

    The client must call NvBufSurfaceSyncForCpu() with the virtual address populated
    by this function before accessing the mapped memory in CPU.

    After memory mapping is complete, mapped memory modification
    must be coordinated between the CPU and hardware device as
    follows:
     - CPU: If the CPU modifies any mapped memory, the client must call
       NvBufSurfaceSyncForDevice() before any hardware device accesses the memory.
     - Hardware device: If the mapped memory is modified by any hardware device,
       the client must call NvBufSurfaceSyncForCpu() before CPU accesses the memory.

     Use NvBufSurfaceUnMap() to unmap buffer(s) and release any resource.

    :arg surf: pointer to NvBufSurface structure.
    :arg index: index of buffer in the batch. -1 for all buffers in batch.
    :arg plane: index of plane in buffer. -1 for all planes in buffer.
    :arg type: flag for mapping type.

    :returns: 0 for success, -1 for failure.
    """


def NvBufSurfaceMapEglImage(surf: NvBufSurface, index: int) -> int:
    """Creates an EGLImage from memory of NvBufSurface buffer(s).

    Only memory type NVBUF_MEM_SURFACE_ARRAY is supported.
    This function will set eglImage pointer of NvBufSurfaceMappedAddr field of
     NvBufSurfaceParams
    with EGLImageKHR.

    This function can be used in scenarios where CUDA operation on Jetson HW
    memory (NVBUF_MEM_SURFACE_ARRAY) is required. EGLImageKHR provided by this
    function can then be register with CUDA for further CUDA operations.

    :arg surf: pointer to NvBufSurface structure.
    :arg index: index of buffer in the batch. -1 for all buffers in batch.

    :returns: 0 for success, -1 for failure.
    """


def NvBufSurfaceMemSet(surf: NvBufSurface, index: int, plane: int, value: int) -> int:
    """Fill each byte of buffer(s) in NvBufSurface with provided value.

    This function can also be used to reset the buffer(s) in the batch.

    :arg surf: pointer to NvBufSurface structure.
    :arg index: index of buffer in the batch. -1 for all buffers in batch.
    :arg plane: index of plane in buffer. -1 for all planes in buffer.
    :arg value: value to be set.

    :returns: 0 for success, -1 for failure.
    """


def NvBufSurfaceSyncForCpu(surf: NvBufSurface, index: int, plane: int) -> int:
    """Syncs the HW memory cache for the CPU.

     Valid only for NVBUF_MEM_SURFACE_ARRAY and NVBUF_MEM_HANDLE memory types.

    :arg surf: pointer to NvBufSurface structure.
    :arg index: index of buffer in the batch. -1 for all buffers in batch.
    :arg plane: index of plane in buffer. -1 for all planes in buffer.

    :returns: 0 for success, -1 for failure.
    """


def NvBufSurfaceSyncForDevice(surf: NvBufSurface, index: int, plane: int) -> int:
    """Syncs the HW memory cache for the device.

    Valid only for NVBUF_MEM_SURFACE_ARRAY and NVBUF_MEM_HANDLE memory types.

    :arg surf: pointer to NvBufSurface structure.
    :arg index: index of buffer in the batch. -1 for all buffers in batch.
    :arg plane: index of plane in buffer. -1 for all planes in buffer.

    :returns: 0 for success, -1 for failure.
    """


def NvBufSurfaceUnMap(surf: NvBufSurface, index: int, plane: int) -> int:
    """Unmap the previously mapped buffer(s).

    :arg surf: pointer to NvBufSurface structure.
    :arg index: index of buffer in the batch. -1 for all buffers in batch.
    :arg plane:index of plane in buffer. -1 for all planes in buffer.

    :returns: 0 for success, -1 for failure.
    """


def alloc_buffer(arg0: int) -> int: ...
def alloc_char_buffer(arg0: int) -> int: ...
def alloc_nvds_event() -> NvDsEvent: ...
def alloc_nvds_event_msg_meta() -> NvDsEventMsgMeta: ...
def alloc_nvds_face_object() -> NvDsFaceObject: ...
def alloc_nvds_payload() -> NvDsPayload: ...
def alloc_nvds_person_object() -> NvDsPersonObject: ...
def alloc_nvds_vehicle_object() -> NvDsVehicleObject: ...
def free_buffer(arg0: int) -> None: ...
def free_gbuffer(arg0: typing.Any) -> None: ...
def generate_ts_rfc3339(arg0: int, arg1: int) -> None: ...
def get_detections(arg0: typing.Any, arg1: int) -> float: ...
def get_nvds_LayerInfo(arg0: typing.Any, arg1: int) -> NvDsInferLayerInfo: ...
def get_nvds_buf_surface(input: int, input1: int) -> numpy.ndarray:
    """This function returns the frame in NumPy format. Only RGBA format is supported.
    For x86_64, only unified memory is supported. For Jetson, the buffer is mapped to
    CPU memory. Changes to the frame image will be preserved and seen in downstream
    elements, with the following restrictions.
        1. No change to image color format or resolution
        2. No transpose operation on the array.

    :arg input: address of the Gstbuffer which contains `NvBufSurface`
    :arg input1: batch_id of the frame to be processed. This indicates the frame's
    index within `NvBufSurface`
    """


def get_optical_flow_vectors(
    of_meta: capsule[NvDsOpticalFlowMeta],
) -> NDArray[numpy.float32]:
    """:arg of_meta: An object of type :class:`NvDsOpticalFlowMeta`

    :returns: Interleaved x, y directed optical flow vectors for
    a block of pixels in numpy format with shape (rows,cols,2),
    where rows and cols are the Optical flow outputs.
    These rows and cols are not eqivalent to input resolution.
    """


def get_ptr(arg0: typing.Any) -> int: ...
def get_segmentation_masks(input: capsule[NvDsInferSegmentationMeta]) -> numpy.ndarray:
    """This function returns the infered masks in Numpy format in the height X width
    shape, these height and width are obtained from the `NvDsInferSegmentationMeta`.
    :arg input: An object of type:class`NvDsInferSegmentationMeta`
    """


def get_string(arg0: int) -> str: ...
def glist_get_nvds_Surface_Params(arg0: typing.Any) -> NvBufSurfaceParams: ...
def glist_get_nvds_batch_meta(arg0: typing.Any) -> NvDsBatchMeta: ...
def glist_get_nvds_classifier_meta(arg0: typing.Any) -> NvDsClassifierMeta: ...
def glist_get_nvds_display_meta(arg0: typing.Any) -> NvDsDisplayMeta: ...
@typing.overload
def glist_get_nvds_event_msg_meta(arg0: typing.Any) -> NvDsEventMsgMeta: ...
@typing.overload
def glist_get_nvds_event_msg_meta(arg0: int) -> NvDsEventMsgMeta: ...
def glist_get_nvds_frame_meta(arg0: typing.Any) -> NvDsFrameMeta: ...
def glist_get_nvds_label_info(arg0: typing.Any) -> NvDsLabelInfo: ...
def glist_get_nvds_object_meta(arg0: typing.Any) -> NvDsObjectMeta: ...
def glist_get_nvds_person_object(arg0: typing.Any) -> NvDsPersonObject: ...
def glist_get_nvds_tensor_meta(arg0: typing.Any) -> NvDsInferTensorMeta: ...
def glist_get_nvds_user_meta(arg0: typing.Any) -> NvDsUserMeta: ...
def glist_get_nvds_vehicle_object(arg0: typing.Any) -> NvDsVehicleObject: ...
def gst_buffer_add_nvds_meta(
    buffer: Gst.Buffer,
    meta_data: typing.Any,
    user_data: typing.Any,
    copy_func: ...,
    release_func: ...,
) -> NvDsMeta:
    """Adds GstMeta of type :class:`NvDsMeta` to the GstBuffer and sets the `meta_data`
    member of :class:`NvDsMeta`.

    :arg buffer: GstBuffer to which the function adds metadata.
    :arg meta_data: The object to which the function sets the meta_data
                member of :class:`NvDsMeta`.
    :arg user_data: A user specific data object
    :arg copy_func: The NvDsMetaCopyFunc function to be called when
                NvDsMeta is to be copied. The function is called with
                meta_data and user_data as parameters.
    :arg release_func: The NvDsMetaReleaseFunc function to be called when
                NvDsMeta is to be destroyed. The function is called with
                meta_data and user_data as parameters.

    :returns: A object to the attached :class:`NvDsMeta` object; or NONE in case failure
    """


def gst_buffer_get_nvds_batch_meta(arg0: int) -> NvDsBatchMeta: ...
def memdup(arg0: int, arg1: int) -> int: ...
def nvds_acquire_classifier_meta_from_pool(
    batch_meta: NvDsBatchMeta,
) -> NvDsClassifierMeta:
    """Acquires :class:`NvDsClassifierMeta` from the classifier meta pool
    User must acquire the classifier meta from the classifier meta pool to
    fill classifier metatada

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` from which
    :class:`NvDsClassifierMeta` will be acquired

    :returns: acquired :class:`NvDsClassifierMeta` object from classifier meta pool
    """


def nvds_acquire_display_meta_from_pool(batch_meta: NvDsBatchMeta) -> NvDsDisplayMeta:
    """Acquires NvDsDisplayMeta from the display meta pool
      User must acquire the display meta from the display meta pool to
     fill display metatada

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` from which
                 :class:`NvDsDisplayMeta` will be acquired.

     :returns: acquired :class:`NvDsDisplayMeta` object from display meta pool
    """


def nvds_acquire_frame_meta_from_pool(batch_meta: NvDsBatchMeta) -> NvDsFrameMeta:
    """Acquires :class:`NvDsFrameMeta` from frame_meta pool. User must acquire the
    frame_meta from frame_meta pool to fill frame metatada.

    :arg  batch_meta: An object of type :class:`NvDsBatchMeta` from which
    :class:`NvDsFrameMeta` will be acquired

        :returns: acquired :class:`NvDsFrameMeta` object from frame meta pool
    """


def nvds_acquire_label_info_meta_from_pool(batch_meta: NvDsBatchMeta) -> NvDsLabelInfo:
    """Acquires :class:`NvDsLabelInfo` from the labelinfo meta pool
     User must acquire the labelinfo meta from the labelinfo meta pool to
    fill labelinfo metatada

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` from which
                :class:`NvDsLabelInfo` will be acquired

    :returns: An object of type :class:`NvDsLabelInfo` object from label info meta pool
    """


def nvds_acquire_meta_lock(input: NvDsBatchMeta) -> None:
    """Lock to be acquired before updating metadata

    :arg input: An object of type :class:`NvDsBatchMeta`
    """


def nvds_acquire_obj_meta_from_pool(batch_meta: NvDsBatchMeta) -> NvDsObjectMeta:
    """Acquires :class:`NvDsObjectMeta` from the object meta pool
    User must acquire the object meta from the object meta pool to fill object metatada

                :arg batch_meta: An object of type :class:`NvDsBatchMeta` from which
                :class:`NvDsObjectMeta` will be acquired

                :returns: acquired :class:`NvDsObjectMeta` object from object meta pool
    """


def nvds_acquire_user_meta_from_pool(batch_meta: NvDsBatchMeta) -> NvDsUserMeta:
    """Acquires NvDsUserMeta from the user meta pool
     User must acquire the user meta from the user meta pool to
    fill user metatada

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` from which
    :class:`NvDsUserMeta`
                will be acquired
    """


def nvds_add_classifier_meta_to_object(
    obj_meta: NvDsObjectMeta, classifier_meta: NvDsClassifierMeta
) -> None:
    """After acquiring and filling classifier metadata user must add
    it to the object metadata with this API

    :arg obj_meta: An object of type :class:`NvDsObjectMeta` to which classifier_meta
    will be attached.
    :arg classifier_meta: An object of type :class:`NvDsClassifierMeta` acquired from
    classifier_meta_pool present in @ref NvDsBatchMeta.
    """


def nvds_add_display_meta_to_frame(
    frame_meta: NvDsFrameMeta, display_meta: NvDsDisplayMeta
) -> None:
    """After acquiring and filling classifier metadata user must add
     it to the frame metadata with this API

    :arg frame_meta: An object of type :class:`NvDsFrameMeta` to which display_meta will
    be attached.
    :arg display_meta: An object of type :class:`NvDsDisplayMeta` acquired from
    display_meta_pool present in @ref NvDsBatchMeta.
    """


def nvds_add_frame_meta_to_batch(
    batch_meta: NvDsBatchMeta, frame_meta: NvDsFrameMeta
) -> None:
    """After acquiring and filling frame metadata, user must add it to the batch
    metadata with this API

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` to which frame_meta will
    be attached.
    :arg frame_meta: An object of type :class:`NvDsFrameMeta` acquired from
    frame_meta_pool present in :class:`NvDsBatchMeta`
    """


def nvds_add_label_info_meta_to_classifier(
    classifier_meta: NvDsClassifierMeta, label_info_meta: typing.Any
) -> None:
    """After acquiring and filling labelinfo metadata user must add
    it to the classifier metadata with this API

     :arg classifier_meta: An object of type :class:`NvDsClassifierMeta` to which
                label_info_meta will be attached.
     :arg label_info_meta: An object of type :class:`NvDsLabelInfo` acquired from
                label_info_meta_pool present in :class:`NvDsBatchMeta`.
    """


def nvds_add_obj_meta_to_frame(
    frame_meta: NvDsFrameMeta, obj_meta: NvDsObjectMeta, obj_parent: NvDsObjectMeta
) -> None:
    """After acquiring and filling object metadata user must add
    it to the frame metadata with this API

    :arg frame_meta: An object of type :class:`NvDsFrameMeta` to which obj_meta will be
    attached.
    :arg obj_meta: An object of type :class:`NvDsObjectMeta` acquired from obj_meta_pool
    present in :class:`NvDsBatchMeta`.
    :arg obj_parent: A parent object of type :class:`NvDsObjectMeta`.This will set the
    parent object's to  obj_meta
    """


def nvds_add_user_meta_to_batch(
    batch_meta: NvDsBatchMeta, user_meta: NvDsUserMeta
) -> None:
    """After acquiring and filling user metadata user must add
    it to batch metadata if required at batch level with this API

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` to which user_meta
              will be attached.
    :arg user_meta: An object of type :class:`NvDsUserMeta` acquired from
             user_meta_pool present in :class:`NvDsBatchMeta`.
    """


def nvds_add_user_meta_to_frame(
    frame_meta: NvDsFrameMeta, user_meta: NvDsUserMeta
) -> None:
    """After acquiring and filling user metadata user must add
    it to frame metadata if required at frame level with this API

    :arg frame_meta: An object of type :class:`NvDsFrameMeta` to which user_meta
               will be attached.
    :arg user_meta: An object of type :class:`NvDsUserMeta` acquired from
                user_meta_pool present in :class:`NvDsBatchMeta`.
    """


def nvds_add_user_meta_to_obj(
    obj_meta: NvDsObjectMeta, user_meta: NvDsUserMeta
) -> None:
    """After acquiring and filling user metadata user must add
     it to object metadata if required at object level with this API

    :arg obj_meta: An object of type :class:`NvDsObjectMeta` to which user_meta
                will be attached.
    :arg user_meta: An object of type :class:`NvDsUserMeta` acquired from
                user_meta_pool present :class:`NvDsBatchMeta`.
    """


def nvds_batch_meta_copy_func(
    data: capsule[NvDsBatchMeta], user_data: typing.Any
) -> capsule:
    """Copy function to copy batch_meta
     It is called when meta_data needs to copied / transformed
    from one buffer to other. meta_data and user_data are passed as arguments.

     :arg data: An object of type :class:`NvDsBatchMeta`
     :arg user_data: An object of user specific data

     :returns: an object that can be typecasted tot :class:`NvDsBatchMeta`
    """


def nvds_batch_meta_release_func(
    data: capsule[NvDsBatchMeta], user_data: typing.Any
) -> None:
    """batch_meta release function called when meta_data is going to be released.

    :arg data: An object of type :class:`NvDsBatchMeta`
    :arg user_data: An object of user specific data
    """


def nvds_clear_batch_user_meta_list(
    batch_meta: NvDsBatchMeta, meta_list: NvDsUserMetaList
) -> None:
    """Removes all the user metadata present in the batch metadata

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` from which
                :class:`NvDsUserMetaList` needs to be cleared
    :arg meta_list: An object of type :class:`NvDsUserMetaList` which needs to be
           cleared
    """


NvDisplayMetaList: typing.TypeAlias = typing.Optional[GList[NvDsDisplayMeta]]


def nvds_clear_display_meta_list(
    frame_meta: NvDsFrameMeta, meta_list: NvDisplayMetaList
) -> None:
    """Removes all the display metadata present in the frame metadata

    :arg frame_meta: An object of type :class:`NvDsFrameMeta` from which
    :class:`NvDisplayMetaList` needs to be cleared
    :arg meta_list: An object of type :class:`NvDisplayMetaList` which needs to be
    cleared
    """


NvDsFrameMetaList: typing.TypeAlias = typing.Optional[GList[NvDsFrameMeta]]


def nvds_clear_frame_meta_list(
    batch_meta: NvDsBatchMeta, meta_list: NvDsFrameMetaList
) -> None:
    """Removes all the frame metadata present in the batch metadata

    :arg batch_meta: An object type of :class:`NvDsBatchMeta` from which
               :class:`NvDsFrameMetaList` needs to be cleared
    :arg  meta_list: An object of type :class:`NvDsFrameMetaList` which needs to be
    cleared
    """


NvDsUserMetaList: typing.TypeAlias = typing.Optional[GList[NvDsUserMeta]]


def nvds_clear_frame_user_meta_list(
    frame_meta: NvDsFrameMeta, meta_list: NvDsUserMetaList
) -> None:
    """Removes all the user metadata present in the frame metadata

    :arg frame_meta: An object of type :class:`NvDsFrameMeta` from which
               :class:`NvDsUserMetaList` needs to be cleared
    :arg meta_list: An object of type :class:`NvDsUserMetaList` which needs to be
                cleared
    """


def nvds_clear_meta_list(
    batch_meta: NvDsBatchMeta, meta_list: NvDsMetaList, meta_pool: NvDsMetaPool
) -> NvDsMetaList:
    """Removes all the metadata elements present in the given metadata list

    :arg batch_meta: An object of type :class:`NvDsBatchMeta`
    :arg meta_list: An object of type :class:`NvDsMetaList` which needs to be cleared
    :arg meta_pool: An object of type :class:`NvDsMetaPool` to which list belongs to

    :returns: an object of updated meta list
    """


NvDsObjectMetaList: typing.TypeAlias = typing.Optional[GList[NvDsObjectMeta]]


def nvds_clear_obj_meta_list(
    frame_meta: NvDsFrameMeta, meta_list: NvDsObjectMetaList
) -> None:
    """Removes all the object metadata present in the frame metadata

        :arg frame_meta: An object of type :class:`NvDsFrameMeta` from which
                    :class:`NvDsObjectMetaList` needs to be cleared
        :arg meta_list: An object of type :class:`NvDsObjectMetaList` which needs to be
                    cleared
        )pyds;




    constexpr const char* nvds_clear_label_info_meta_list=R"pyds(
    removes all the label info metadata present in classifier metadata

        :arg classifier_meta: An object of type :class:`NvDsClassifierMeta` from which
                    :class:`NvDsLabelInfoList` needs to be cleared
        :arg meta_list: An object of type :class:`NvDsLabelInfoList` which needs to be
                    cleared
    """


def nvds_clear_obj_user_meta_list(
    object_meta: NvDsObjectMeta, meta_list: NvDsObjectMetaList
) -> None:
    """Removes all the user metadata present in the object metadata

    :arg object_meta: An object of type :class:`NvDsObjectMeta` from which
                :class:`NvDsUserMetaList` needs to be cleared
    :arg meta_list: An object of type :class:`NvDsUserMetaList` which needs to be
                cleared
    """


def nvds_copy_batch_user_meta_list(
    src_user_meta_list: NvDsObjectMetaList, dst_batch_meta: NvDsBatchMeta
) -> None:
    """Deep copy of src_user_meta_list to user meta list present in the
    dst_batch_meta.

    :arg src_user_meta_list: An obect of type :class:`NvDsUserMetaList`
    :arg dst_batch_meta: An object of type :class:`NvDsBatchMeta`
    """


def nvds_copy_display_meta_list(
    src_display_meta_list: NvDisplayMetaList, dst_frame_meta: NvDsFrameMeta
) -> None:
    """Deep copy of src_display_meta_list to display meta list present in the
    dst_frame_meta.

    :arg src_display_meta_list: An object of type :class:`NvDisplayMetaList`
    :arg dst_frame_meta: An object of type :class:`NvDsFrameMeta`
    """


@typing.overload
def nvds_copy_frame_meta_list(
    src_frame_meta_list: NvDsFrameMetaList, dst_batch_meta: NvDsBatchMeta
) -> None:
    """Deep copy of src_frame_meta_list to frame meta list present in the
        dst_batch_meta.

    :arg src_frame_meta_list: An object of type :class:`NvDsFrameMetaList`
    :arg dst_batch_meta: An object of type :class:`NvDsBatchMeta`
    """


@typing.overload
def nvds_copy_frame_meta_list(arg0: NvDsFrameMetaList, arg1: NvDsBatchMeta) -> None: ...
def nvds_copy_frame_user_meta_list(
    src_user_meta_list: NvDsUserMetaList, dst_frame_meta: NvDsFrameMeta
) -> None:
    """Deep copy of src_user_meta_list to user meta list present in the
    dst_frame_meta.

    :arg src_user_meta_list: An object of type :class:`NvDsUserMetaList`
    :arg dst_frame_meta: An object of type :class:`NvDsFrameMeta`
    """


def nvds_copy_obj_meta_list(
    src_obj_meta_list: NvDsObjectMetaList, dst_frame_meta: NvDsFrameMeta
) -> None:
    """Deep copy of src_obj_meta_list to frame meta list present in the
      dst_frame_meta.

    :arg src_obj_meta_list: An object of type :class:`NvDsObjectMetaList`
    :arg dst_frame_meta: An object of type :class:`NvDsFrameMeta`
    """


def nvds_create_batch_meta(max_batch_size: int) -> NvDsBatchMeta:
    """Creates a :class:`NvDsBatchMeta` of given batch size.

    :arg max_batch_size: maximum number of frames those can be present in the batch
        :returns: allocated :class:`NvDsBatchMeta` object
    """


def nvds_destroy_batch_meta(batch_meta: NvDsBatchMeta) -> int:
    """Deletes/Releases :class:`NvDsBatchMeta` batch_meta object

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` to be deleted/destroyed
    after use
    """


def nvds_get_current_metadata_info(batch_meta: NvDsBatchMeta) -> int:
    """Debug function to get current metadata info

    :arg batch_meta: An object of type :class:`NvDsBatchMeta`
    """


def nvds_get_nth_frame_meta(
    frame_meta_list: GList[NvDsFrameMeta], index: int
) -> NvDsFrameMeta:
    """:arg frame_meta_list: A list of objects of type :class:`NvDsFrameMeta`
    :arg index: index at which  :class:`NvDsFrameMeta` object needs to be accessed.

    :returns:  an object of type :class:`NvDsFrameMeta` from frame_meta_list
    """


def nvds_get_user_meta_type(meta_descriptor: str) -> NvDsMetaType:
    """Generates a unique user metadata type from the given string describing
        user specific metadata.

    :arg meta_descriptor: A string object describing metadata.
                The format of the string should be specified as below
                ORG_NAME.COMPONENT_NAME.METADATA_DESCRIPTION.
                e.g. (NVIDIA.NVINFER.TENSOR_METADATA)
    """


def nvds_release_meta_lock(input: NvDsBatchMeta) -> None:
    """Lock to be released after updating metadata

    :arg input: An object of type :class:`NvDsBatchMeta`
    """


def nvds_remove_classifier_meta_from_obj(
    obj_meta: NvDsObjectMeta, classifier_meta: NvDsClassifierMeta
) -> None:
    """Removes given classifier meta from object metadata

    :arg obj_meta: An object of type :class:`NvDsObjectMeta` from which classifier_meta
    is to be removed.
    :arg classifier_meta: An object of type :class:`NvDsClassifierMeta` to be removed
    from
    obj_meta.
    """


def nvds_remove_display_meta_from_frame(
    frame_meta: NvDsFrameMeta, display_meta: NvDsDisplayMeta
) -> None:
    """Removes given display meta from frame metadata

    :arg frame_meta: An object of type :class:`NvDsFrameMeta` from which display_meta
               is to be removed.
    :arg display_meta: An object of type :class:`NvDsDisplayMeta` to be removed from
       frame_meta.
    """


def nvds_remove_frame_meta_from_batch(
    batch_meta: NvDsBatchMeta, frame_meta: NvDsFrameMeta
) -> None:
    """Removes given frame meta from the batch metadata

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` from which frame_meta is
    to be removed.
    :arg frame_meta: A object of type :class:`NvDsFrameMeta` to be removed from
    batch_meta.
    """


def nvds_remove_label_info_meta_from_classifier(
    classifier_meta: NvDsClassifierMeta, label_info_meta: NvDsLabelInfo
) -> None:
    """Removes given labelinfo meta from the classifier metadata

     :arg classifier_meta: An object of type :class:`NvDsClassifierMeta` from which
                label_info_meta is to be removed.
    :arg label_info_meta: An object of type :class:`NvDsLabelInfo` to be removed from
               classifier_meta.
    """


def nvds_remove_obj_meta_from_frame(
    frame_meta: NvDsFrameMeta, obj_meta: NvDsObjectMeta
) -> None:
    """Removes given object meta from the frame metadata

    :arg frame_meta: An object of type :class:`NvDsFrameMeta` from which obj_meta
               is to be removed.
    :arg obj_meta: An object of type :class:`NvDsObjectMeta` to be removed from
               frame_meta.
    """


def nvds_remove_user_meta_from_batch(
    batch_meta: NvDsBatchMeta, user_meta: NvDsUserMeta
) -> None:
    """Removes given user metadata from the batch metadata

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` from which user_meta
            is to be removed.
    :arg user_meta: An object of type :class:`NvDsUserMeta` to be removed from
               batch_meta.

     :returns: acquired :class:`NvDsUserMeta` object from user meta pool
    """


def nvds_remove_user_meta_from_frame(
    frame_meta: NvDsFrameMeta, user_meta: NvDsUserMeta
) -> None:
    """Removes given user metadata from the frame metadata

     :arg frame_meta: An object of type :class:`NvDsFrameMeta` from which user_meta
                 is to be removed.
    :arg user_meta: An object of type :class:`NvDsUserMeta` to be removed from
                 frame_meta.
    """


def nvds_remove_user_meta_from_object(
    obj_meta: NvDsObjectMeta, user_meta: NvDsUserMeta
) -> None:
    """Removes given user metadata from the object metadata

    :arg obj_meta: An object of type :class:`NvDsObjectMeta` from which user_meta
                is to be removed.
    :arg user_meta: An object of type :class:`NvDsUserMeta` to be removed from
                obj_meta.
    """


def register_user_copyfunc(
    arg0: typing.Callable[[typing.Any, typing.Any], typing.Any],
) -> None: ...
def register_user_releasefunc(
    arg0: typing.Callable[[typing.Any, typing.Any], None],
) -> None: ...
def set_user_copyfunc(
    arg0: NvDsUserMeta, arg1: typing.Callable[[typing.Any, typing.Any], typing.Any]
) -> None: ...
def set_user_releasefunc(
    arg0: NvDsUserMeta, arg1: typing.Callable[[typing.Any, typing.Any], None]
) -> None: ...
def strdup(arg0: int) -> int: ...
def strdup2str(arg0: int) -> str: ...
def unset_callback_funcs() -> None: ...
def user_copyfunc(
    arg0: NvDsUserMeta, arg1: typing.Callable[[typing.Any, typing.Any], typing.Any]
) -> None: ...
def user_releasefunc(
    arg0: NvDsUserMeta, arg1: typing.Callable[[typing.Any, typing.Any], None]
) -> None: ...


BOTH_HEAD: NvOSD_Arrow_Head_Direction  # value = NvOSD_Arrow_Head_Direction.BOTH_HEAD
END_HEAD: NvOSD_Arrow_Head_Direction  # value = NvOSD_Arrow_Head_Direction.END_HEAD
FLOAT: NvDsInferDataType  # value = NvDsInferDataType.FLOAT
HALF: NvDsInferDataType  # value = NvDsInferDataType.HALF
INSIDE_AISLE_360D: ROI_STATUS_360D  # value = ROI_STATUS_360D.INSIDE_AISLE_360D
INT32: NvDsInferDataType  # value = NvDsInferDataType.INT32
INT8: NvDsInferDataType  # value = NvDsInferDataType.INT8
MODE_CPU: NvOSD_Mode  # value = NvOSD_Mode.MODE_CPU
MODE_GPU: NvOSD_Mode  # value = NvOSD_Mode.MODE_GPU
MODE_HW: NvOSD_Mode  # value = NvOSD_Mode.MODE_HW
NVBUF_COLOR_FORMAT_ABGR: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_ABGR

NVBUF_COLOR_FORMAT_ARGB: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_ARGB
NVBUF_COLOR_FORMAT_BGR: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_BGR
NVBUF_COLOR_FORMAT_BGRA: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_BGRA
NVBUF_COLOR_FORMAT_BGRx: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_BGRx
NVBUF_COLOR_FORMAT_GRAY8: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_GRAY8
NVBUF_COLOR_FORMAT_INVALID: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_INVALID
NVBUF_COLOR_FORMAT_LAST: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_LAST
NVBUF_COLOR_FORMAT_NV12: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12
NVBUF_COLOR_FORMAT_NV12_10LE: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE
NVBUF_COLOR_FORMAT_NV12_10LE_2020: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE_2020
NVBUF_COLOR_FORMAT_NV12_10LE_709: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE_709
NVBUF_COLOR_FORMAT_NV12_10LE_709_ER: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE_709_ER
NVBUF_COLOR_FORMAT_NV12_10LE_ER: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE_ER
NVBUF_COLOR_FORMAT_NV12_12LE: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_12LE
NVBUF_COLOR_FORMAT_NV12_2020: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_2020
NVBUF_COLOR_FORMAT_NV12_709: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_709
NVBUF_COLOR_FORMAT_NV12_709_ER: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_709_ER
NVBUF_COLOR_FORMAT_NV12_ER: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_ER
NVBUF_COLOR_FORMAT_NV21: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV21
NVBUF_COLOR_FORMAT_NV21_ER: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV21_ER
NVBUF_COLOR_FORMAT_RGB: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_RGB
NVBUF_COLOR_FORMAT_RGBA: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_RGBA
NVBUF_COLOR_FORMAT_RGBx: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_RGBx
NVBUF_COLOR_FORMAT_SIGNED_R16G16: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_SIGNED_R16G16
NVBUF_COLOR_FORMAT_UYVY: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_UYVY
NVBUF_COLOR_FORMAT_UYVY_ER: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_UYVY_ER
NVBUF_COLOR_FORMAT_VYUY: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_VYUY
NVBUF_COLOR_FORMAT_VYUY_ER: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_VYUY_ER
NVBUF_COLOR_FORMAT_YUV420: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420
NVBUF_COLOR_FORMAT_YUV420_2020: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420_2020
NVBUF_COLOR_FORMAT_YUV420_709: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420_709
NVBUF_COLOR_FORMAT_YUV420_709_ER: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420_709_ER
NVBUF_COLOR_FORMAT_YUV420_ER: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420_ER
NVBUF_COLOR_FORMAT_YUV444: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV444
NVBUF_COLOR_FORMAT_YUYV: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUYV
NVBUF_COLOR_FORMAT_YUYV_ER: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUYV_ER
NVBUF_COLOR_FORMAT_YVU420: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YVU420
NVBUF_COLOR_FORMAT_YVU420_ER: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YVU420_ER
NVBUF_COLOR_FORMAT_YVYU: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YVYU
NVBUF_COLOR_FORMAT_YVYU_ER: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YVYU_ER
NVBUF_COLOR_FORMAT_xBGR: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_xBGR
NVBUF_COLOR_FORMAT_xRGB: NvBufSurfaceColorFormat
# value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_xRGB
NVBUF_LAYOUT_BLOCK_LINEAR: NvBufSurfaceLayout
# value = NvBufSurfaceLayout.NVBUF_LAYOUT_BLOCK_LINEAR
NVBUF_LAYOUT_PITCH: NvBufSurfaceLayout
# value = NvBufSurfaceLayout.NVBUF_LAYOUT_PITCH
NVBUF_MAP_READ: NvBufSurfaceMemMapFlags
# value = NvBufSurfaceMemMapFlags.NVBUF_MAP_READ
NVBUF_MAP_READ_WRITE: NvBufSurfaceMemMapFlags
# value = NvBufSurfaceMemMapFlags.NVBUF_MAP_READ_WRITE
NVBUF_MAP_WRITE: NvBufSurfaceMemMapFlags
# value = NvBufSurfaceMemMapFlags.NVBUF_MAP_WRITE
NVBUF_MEM_CUDA_DEVICE: NvBufSurfaceMemType
# value = NvBufSurfaceMemType.NVBUF_MEM_CUDA_DEVICE
NVBUF_MEM_CUDA_PINNED: NvBufSurfaceMemType
# value = NvBufSurfaceMemType.NVBUF_MEM_CUDA_PINNED
NVBUF_MEM_CUDA_UNIFIED: NvBufSurfaceMemType
# value = NvBufSurfaceMemType.NVBUF_MEM_CUDA_UNIFIED
NVBUF_MEM_DEFAULT: NvBufSurfaceMemType  # value = NvBufSurfaceMemType.NVBUF_MEM_DEFAULT
NVBUF_MEM_HANDLE: NvBufSurfaceMemType  # value = NvBufSurfaceMemType.NVBUF_MEM_HANDLE
NVBUF_MEM_SURFACE_ARRAY: NvBufSurfaceMemType
# value = NvBufSurfaceMemType.NVBUF_MEM_SURFACE_ARRAY
NVBUF_MEM_SYSTEM: NvBufSurfaceMemType  # value = NvBufSurfaceMemType.NVBUF_MEM_SYSTEM
NVDSINFER_SEGMENTATION_META: NvDsMetaType
# value = NvDsMetaType.NVDSINFER_SEGMENTATION_META
NVDSINFER_TENSOR_OUTPUT_META: NvDsMetaType
# value = NvDsMetaType.NVDSINFER_TENSOR_OUTPUT_META
NVDS_AUDIO_BATCH_META: NvDsMetaType  # value = NvDsMetaType.NVDS_AUDIO_BATCH_META
NVDS_AUDIO_FRAME_META: NvDsMetaType  # value = NvDsMetaType.NVDS_AUDIO_FRAME_META
NVDS_BATCH_GST_META: GstNvDsMetaType  # value = GstNvDsMetaType.NVDS_BATCH_GST_META
NVDS_BATCH_META: NvDsMetaType  # value = NvDsMetaType.NVDS_BATCH_META
NVDS_CLASSIFIER_META: NvDsMetaType  # value = NvDsMetaType.NVDS_CLASSIFIER_META
NVDS_CROP_IMAGE_META: NvDsMetaType  # value = NvDsMetaType.NVDS_CROP_IMAGE_META
NVDS_DECODER_GST_META: GstNvDsMetaType  # value = GstNvDsMetaType.NVDS_DECODER_GST_META
NVDS_DEWARPER_GST_META: GstNvDsMetaType
# value = GstNvDsMetaType.NVDS_DEWARPER_GST_META
NVDS_DISPLAY_META: NvDsMetaType  # value = NvDsMetaType.NVDS_DISPLAY_META
NVDS_EVENT_CUSTOM: NvDsEventType  # value = NvDsEventType.NVDS_EVENT_CUSTOM
NVDS_EVENT_EMPTY: NvDsEventType  # value = NvDsEventType.NVDS_EVENT_EMPTY
NVDS_EVENT_ENTRY: NvDsEventType  # value = NvDsEventType.NVDS_EVENT_ENTRY
NVDS_EVENT_EXIT: NvDsEventType  # value = NvDsEventType.NVDS_EVENT_EXIT
NVDS_EVENT_FORCE32: NvDsEventType  # value = NvDsEventType.NVDS_EVENT_FORCE32
NVDS_EVENT_MOVING: NvDsEventType  # value = NvDsEventType.NVDS_EVENT_MOVING
NVDS_EVENT_MSG_META: NvDsMetaType  # value = NvDsMetaType.NVDS_EVENT_MSG_META
NVDS_EVENT_PARKED: NvDsEventType  # value = NvDsEventType.NVDS_EVENT_PARKED
NVDS_EVENT_RESERVED: NvDsEventType  # value = NvDsEventType.NVDS_EVENT_RESERVED
NVDS_EVENT_RESET: NvDsEventType  # value = NvDsEventType.NVDS_EVENT_RESET
NVDS_EVENT_STOPPED: NvDsEventType  # value = NvDsEventType.NVDS_EVENT_STOPPED
NVDS_FORCE32_META: NvDsMetaType  # value = NvDsMetaType.NVDS_FORCE32_META
NVDS_FRAME_META: NvDsMetaType  # value = NvDsMetaType.NVDS_FRAME_META
NVDS_GST_CUSTOM_META: NvDsMetaType  # value = NvDsMetaType.NVDS_GST_CUSTOM_META
NVDS_GST_INVALID_META: GstNvDsMetaType  # value = GstNvDsMetaType.NVDS_GST_INVALID_META
NVDS_GST_META_FORCE32: GstNvDsMetaType  # value = GstNvDsMetaType.NVDS_GST_META_FORCE32
NVDS_INVALID_META: NvDsMetaType  # value = NvDsMetaType.NVDS_INVALID_META
NVDS_LABEL_INFO_META: NvDsMetaType  # value = NvDsMetaType.NVDS_LABEL_INFO_META
NVDS_LATENCY_MEASUREMENT_META: NvDsMetaType
# value = NvDsMetaType.NVDS_LATENCY_MEASUREMENT_META
NVDS_OBEJCT_TYPE_FORCE32: NvDsObjectType
# value = NvDsObjectType.NVDS_OBEJCT_TYPE_FORCE32
NVDS_OBJECT_TYPE_BAG: NvDsObjectType  # value = NvDsObjectType.NVDS_OBJECT_TYPE_BAG
NVDS_OBJECT_TYPE_BICYCLE: NvDsObjectType
# value = NvDsObjectType.NVDS_OBJECT_TYPE_BICYCLE
NVDS_OBJECT_TYPE_CUSTOM: NvDsObjectType
# value = NvDsObjectType.NVDS_OBJECT_TYPE_CUSTOM
NVDS_OBJECT_TYPE_FACE: NvDsObjectType  # value = NvDsObjectType.NVDS_OBJECT_TYPE_FACE
NVDS_OBJECT_TYPE_FACE_EXT: NvDsObjectType
# value = NvDsObjectType.NVDS_OBJECT_TYPE_FACE_EXT
NVDS_OBJECT_TYPE_PERSON: NvDsObjectType
# value = NvDsObjectType.NVDS_OBJECT_TYPE_PERSON
NVDS_OBJECT_TYPE_PERSON_EXT: NvDsObjectType
# value = NvDsObjectType.NVDS_OBJECT_TYPE_PERSON_EXT
NVDS_OBJECT_TYPE_RESERVED: NvDsObjectType
# value = NvDsObjectType.NVDS_OBJECT_TYPE_RESERVED
NVDS_OBJECT_TYPE_ROADSIGN: NvDsObjectType
# value = NvDsObjectType.NVDS_OBJECT_TYPE_ROADSIGN
NVDS_OBJECT_TYPE_UNKNOWN: NvDsObjectType
# value = NvDsObjectType.NVDS_OBJECT_TYPE_UNKNOWN
NVDS_OBJECT_TYPE_VEHICLE: NvDsObjectType
# value = NvDsObjectType.NVDS_OBJECT_TYPE_VEHICLE
NVDS_OBJECT_TYPE_VEHICLE_EXT: NvDsObjectType
# value = NvDsObjectType.NVDS_OBJECT_TYPE_VEHICLE_EXT
NVDS_OBJ_META: NvDsMetaType  # value = NvDsMetaType.NVDS_OBJ_META
NVDS_OPTICAL_FLOW_META: NvDsMetaType  # value = NvDsMetaType.NVDS_OPTICAL_FLOW_META
NVDS_PAYLOAD_CUSTOM: NvDsPayloadType  # value = NvDsPayloadType.NVDS_PAYLOAD_CUSTOM
NVDS_PAYLOAD_DEEPSTREAM: NvDsPayloadType
# value = NvDsPayloadType.NVDS_PAYLOAD_DEEPSTREAM
NVDS_PAYLOAD_DEEPSTREAM_MINIMAL: NvDsPayloadType
# value = NvDsPayloadType.NVDS_PAYLOAD_DEEPSTREAM_MINIMAL
NVDS_PAYLOAD_FORCE32: NvDsPayloadType  # value = NvDsPayloadType.NVDS_PAYLOAD_FORCE32
NVDS_PAYLOAD_META: NvDsMetaType  # value = NvDsMetaType.NVDS_PAYLOAD_META
NVDS_PAYLOAD_RESERVED: NvDsPayloadType  # value = NvDsPayloadType.NVDS_PAYLOAD_RESERVED
NVDS_RESERVED_GST_META: GstNvDsMetaType
# value = GstNvDsMetaType.NVDS_RESERVED_GST_META
NVDS_RESERVED_META: NvDsMetaType  # value = NvDsMetaType.NVDS_RESERVED_META
NVDS_START_USER_META: NvDsMetaType  # value = NvDsMetaType.NVDS_START_USER_META
NVDS_TRACKER_PAST_FRAME_META: NvDsMetaType
# value = NvDsMetaType.NVDS_TRACKER_PAST_FRAME_META
NVDS_USER_META: NvDsMetaType  # value = NvDsMetaType.NVDS_USER_META
ROI_ENTRY_360D: ROI_STATUS_360D  # value = ROI_STATUS_360D.ROI_ENTRY_360D
ROI_EXIT_360D: ROI_STATUS_360D  # value = ROI_STATUS_360D.ROI_EXIT_360D
START_HEAD: NvOSD_Arrow_Head_Direction  # value = NvOSD_Arrow_Head_Direction.START_HEAD
__version__: str = "1.0.2"

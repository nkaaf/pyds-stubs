# ruff: noqa: PYI021
# ruff: noqa: N801
# ruff: noqa: N802
# ruff: noqa: N803
# ruff: noqa: N815
# ruff: noqa: D205
# ruff: noqa: D418
# ruff: noqa: A002
# ruff: noqa: ANN002
# ruff: noqa: ANN003
# ruff: noqa: ANN205
# ruff: noqa: ANN401
# ruff: noqa: ERA001

"""pybind11 bindings for gstnvdsmeta."""

import typing

import numpy
from gi.repository import GLib, Gst
from numpy.typing import NDArray

__all__ = [
    "BOTH_HEAD",
    "END_HEAD",
    "FLOAT",
    "HALF",
    "INSIDE_AISLE_360D",
    "INT8",
    "INT32",
    "MODE_CPU",
    "MODE_GPU",
    "MODE_NONE",
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
    "CustomDataStruct",
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
    "NvOSD_MaskParams",
    "NvOSD_Mode",
    "NvOSD_RectParams",
    "NvOSD_TextParams",
    "RectDim",
    "alloc_buffer",
    "alloc_char_buffer",
    "alloc_custom_struct",
    "alloc_nvds_event",
    "alloc_nvds_event_msg_meta",
    "alloc_nvds_face_object",
    "alloc_nvds_payload",
    "alloc_nvds_person_object",
    "alloc_nvds_vehicle_object",
    "configure_source_for_ntp_sync",
    "free_buffer",
    "free_gbuffer",
    "generate_ts_rfc3339",
    "get_detections",
    "get_nvds_LayerInfo",
    "get_nvds_buf_surface",
    "get_nvds_buf_surface_gpu",
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
    "gst_element_send_nvevent_new_stream_reset",
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
    "unmap_nvds_buf_surface",
    "unset_callback_funcs",
    "user_copyfunc",
    "user_releasefunc",
]

from pyds.typing import GList, capsule

class CustomDataStruct:
    """Holds custom struct data.

    :ivar structId: *int*, ID for this struct.
    :ivar message: *str*, Message embedded in this structure.
    :ivar sampleInt: *int*, Sample int data
    """

    sampleInt: int
    structId: int

    def __init__(self) -> None: ...
    def cast(self: capsule[CustomDataStruct]) -> CustomDataStruct:
        """Cast given object/data to :class:`CustomDataStruct`, call
        pyds.CustomDataStruct.cast(data).
        """

    @property
    def message(self) -> int: ...
    @message.setter
    def message(self, arg1: str) -> None: ...

class GstNvDsMetaType:
    """*Enumerator*. Specifies the type of meta data.

    NVIDIA defined :class:`GstNvDsMetaType` values are in the range
    from NVDS_BATCH_GST_META to NVDS_START_USER_META.

    Members:

      NVDS_GST_INVALID_META : NVDS_GST_INVALID_META

      NVDS_BATCH_GST_META : Specifies information of a formed batch.

      NVDS_DECODER_GST_META : NVDS_DECODER_GST_META

      NVDS_DEWARPER_GST_META : Specifies information of dewarped surfaces.

      NVDS_RESERVED_GST_META : NVDS_RESERVED_GST_META

      NVDS_GST_META_FORCE32 : Specifies the first value that may be assigned to a
      user-defined type.
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
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str."""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.GstNvDsMetaType, arg0: int) -> None."""

    def __index__(self) -> int: ...
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...

class NvBbox_Coords:
    """Holds unclipped bounding box coordinates of the object.

    :ivar left: *float*, Holds the box's left coordinate in pixels.
    :ivar top: *float*, Holds the box's top coordinate in pixels.
    :ivar width: *float*, Holds the box's width in pixels.
    :ivar height: *float*, Holds the box's height in pixels.
    """

    height: float
    left: float
    top: float
    width: float

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvBbox_Coords]) -> NvBbox_Coords:
        """Cast given object/data to :class:`NvBbox_Coords`, call
        pyds.NvBbox_Coords.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvBbox_Coords:
        """Cast given object/data to :class:`NvBbox_Coords`, call
        pyds.NvBbox_Coords.cast(data).
        """

class NvBufSurface:
    """Holds information about a single buffer in a batch.

    :ivar gpuId: *int*, Holds the GPU ID. Valid only for a multi-GPU system.
    :ivar batchSize: *int*, Holds the batch size.
    :ivar numFilled: *int*, Holds the number valid and filled buffers. Initialized to
    zero when an instance of the structure is created.
    :ivar isContiguous: *bool*, Holds an "is contiguous" flag. If set,
    memory allocated for the batch is contiguous.
    :ivar memType: :class:`NvBufSurfaceMemType`, Holds type of memory for buffers in
    the batch.
    :ivar surfaceList: *list of :class:`NvBufSurfaceParams`*, Array of batched buffers.
    """

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvBufSurface]) -> NvBufSurface:
        """Cast given object/data to :class:`NvBufSurface`, call
        pyds.NvBufSurface.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvBufSurface:
        """Cast given object/data to :class:`NvBufSurface`, call
        pyds.NvBufSurface.cast(data).
        """

    @property
    def batchSize(self) -> int: ...
    @property
    def gpuId(self) -> int: ...
    @property
    def isContiguous(self) -> bool: ...
    @property
    def memType(self) -> NvBufSurfaceMemType: ...
    @property
    def numFilled(self) -> int: ...
    @property
    def surfaceList(self) -> NvBufSurfaceParams: ...

class NvBufSurfaceColorFormat:
    """*Enumerator*. Specifies color formats for :class:`NvBufSurface`.

    Members:

      NVBUF_COLOR_FORMAT_INVALID : Invalid color format

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

      NVBUF_COLOR_FORMAT_NV12_10LE : BT.601 colorspace - Y/CbCr 4:2:0 10-bit
      multi-planar.

      NVBUF_COLOR_FORMAT_NV12_12LE : BT.601 colorspace - Y/CbCr 4:2:0 12-bit
      multi-planar.

      NVBUF_COLOR_FORMAT_YUV420_709 : BT.709 colorspace - YUV420 multi-planar.

      NVBUF_COLOR_FORMAT_YUV420_709_ER : BT.709 colorspace - YUV420 ER multi-planar.

      NVBUF_COLOR_FORMAT_NV12_709 : BT.709 colorspace - Y/CbCr 4:2:0 multi-planar.

      NVBUF_COLOR_FORMAT_NV12_709_ER : BT.709 colorspace - Y/CbCr ER 4:2:0 multi-planar.

      NVBUF_COLOR_FORMAT_YUV420_2020 : BT.2020 colorspace - YUV420 multi-planar.

      NVBUF_COLOR_FORMAT_NV12_2020 : BT.2020 colorspace - Y/CbCr 4:2:0 multi-planar.

      NVBUF_COLOR_FORMAT_NV12_10LE_ER : BT.601 colorspace - Y/CbCr ER 4:2:0 10-bit
      multi-planar.

      NVBUF_COLOR_FORMAT_NV12_10LE_709 : BT.709 colorspace - Y/CbCr 4:2:0 10-bit
      multi-planar.

      NVBUF_COLOR_FORMAT_NV12_10LE_709_ER : BT.709 colorspace - Y/CbCr ER 4:2:0
      10-bit multi-planar.

      NVBUF_COLOR_FORMAT_NV12_10LE_2020 : BT.2020 colorspace - Y/CbCr 4:2:0 10-bit
      multi-planar.

      NVBUF_COLOR_FORMAT_SIGNED_R16G16 : Color format for packed 2 signed shorts.

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
    __members__: typing.ClassVar[
        dict[str, NvBufSurfaceColorFormat]
    ]  # value = {'NVBUF_COLOR_FORMAT_INVALID':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_INVALID, 'NVBUF_COLOR_FORMAT_GRAY8':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_GRAY8, 'NVBUF_COLOR_FORMAT_YUV420':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420, 'NVBUF_COLOR_FORMAT_YVU420':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YVU420,
    # 'NVBUF_COLOR_FORMAT_YUV420_ER':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420_ER,
    # 'NVBUF_COLOR_FORMAT_YVU420_ER':
    # NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YVU420_ER,
    # 'NVBUF_COLOR_FORMAT_NV12': NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12,
    # 'NVBUF_COLOR_FORMAT_NV12_ER':
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
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str."""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvBufSurfaceColorFormat, arg0: int) -> None."""

    def __index__(self) -> int: ...
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...

class NvBufSurfaceCreateParams:
    """Holds parameters required to allocate an :class:`NvBufSurface`.

    :ivar gpuId: *int*, Holds the GPU ID. Valid only for a multi-GPU system.
    :ivar width: *int*, Holds the width of the buffer.
    :ivar height: *int*, Holds the height of the buffer.
    :ivar size: *int*, Holds the amount of memory to be allocated.
    :ivar isContiguous: *bool*, Holds a "contiguous memory" flag. If set, contiguous
    memory is allocated for the batch. Valid only for CUDA memory types.
    :ivar colorFormat: :class:`NvBufSurfaceColorFormat`, Holds the color format of
    the buffer.
    :ivar layout: :class:`NvBufSurfaceLayout`, Holds the surface layout. May be Block
    Linear (BL) or Pitch Linear (PL).
    :ivar memType: :class:`NvBufSurfaceMemType`, Holds the type of memory to be
    allocated.
    """

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvBufSurfaceCreateParams]) -> NvBufSurfaceCreateParams:
        """Cast given object/data to :class:`NvBufSurfaceCreateParams`, call
        pyds.NvBufSurfaceCreateParams.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvBufSurfaceCreateParams:
        """Cast given object/data to :class:`NvBufSurfaceCreateParams`, call
        pyds.NvBufSurfaceCreateParams.cast(data).
        """

    @property
    def colorFormat(self) -> NvBufSurfaceColorFormat: ...
    @property
    def gpuId(self) -> int: ...
    @property
    def height(self) -> int: ...
    @property
    def isContiguous(self) -> bool: ...
    @property
    def layout(self) -> NvBufSurfaceLayout: ...
    @property
    def memType(self) -> NvBufSurfaceMemType: ...
    @property
    def size(self) -> int: ...
    @property
    def width(self) -> int: ...

class NvBufSurfaceLayout:
    """*Enumerator*. Specifies layout formats for :class:`NvBufSurface` video planes.

    Members:

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
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str."""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvBufSurfaceLayout, arg0: int) -> None."""

    def __index__(self) -> int: ...
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...

class NvBufSurfaceMappedAddr:
    """Holds objects for a mapped buffer.

    :ivar addr: Array for a planewise CPU mapped buffer.
    :ivar eglImage: An object for a mapped EGLImage.
    """

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvBufSurfaceMappedAddr]) -> NvBufSurfaceMappedAddr:
        """Cast given object/data to :class:`NvBufSurfaceMappedAddr`, call
        pyds.NvBufSurfaceMappedAddr.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvBufSurfaceMappedAddr:
        """Cast given object/data to :class:`NvBufSurfaceMappedAddr`, call
        pyds.NvBufSurfaceMappedAddr.cast(data).
        """

    @property
    def addr(self) -> numpy.ndarray: ...
    @addr.setter
    def addr(self) -> None: ...
    @property
    def eglImage(self) -> typing.Any: ...

class NvBufSurfaceMemMapFlags:
    """*Enumerator*. Specifies mapping types for :class:`NvBufSurface`.

    Members:

      NVBUF_MAP_READ : Specifies :class:`NvBufSurface` mapping type "read."

      NVBUF_MAP_WRITE : Specifies :class:`NvBufSurface` mapping type "write."

      NVBUF_MAP_READ_WRITE : Specifies :class:`NvBufSurface` mapping type "read/write."
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
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str."""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvBufSurfaceMemMapFlags, arg0: int) -> None."""

    def __index__(self) -> int: ...
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...

class NvBufSurfaceMemType:
    """Specifies the default memory type, i.e. NVBUF_MEM_CUDA_DEVICE for dGPU,
    NVBUF_MEM_SURFACE_ARRAY for Jetson. Use NVBUF_MEM_DEFAULT to allocate whichever
    type of memory is appropriate for the platform.

    Members:

      NVBUF_MEM_DEFAULT : NVBUF_MEM_CUDA_DEVICE type for dGpu and
      NVBUF_MEM_SURFACE_ARRAY type for Jetson.

      NVBUF_MEM_CUDA_PINNED : CUDA Host memory type.

      NVBUF_MEM_CUDA_DEVICE : CUDA Device memory type.

      NVBUF_MEM_CUDA_UNIFIED : CUDA Unified memory type.

      NVBUF_MEM_SURFACE_ARRAY : NVRM Surface Array type - valid only for Jetson.

      NVBUF_MEM_HANDLE : NVRM Handle type - valid only for Jetson.

      NVBUF_MEM_SYSTEM : Memory allocated by malloc().
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
    # 'NVBUF_MEM_HANDLE': NvBufSurfaceMemType.NVBUF_MEM_HANDLE, 'NVBUF_MEM_SYSTEM':
    # NvBufSurfaceMemType.NVBUF_MEM_SYSTEM}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str."""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvBufSurfaceMemType, arg0: int) -> None."""

    def __index__(self) -> int: ...
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...

class NvBufSurfaceParams:
    """Holds information about a single buffer in a batch.

    :ivar width: *int*, Holds the width of the buffer.
    :ivar height: *int*, Holds the height of the buffer.
    :ivar pitch: *int*, Holds the pitch of the buffer.
    :ivar colorFormat: :class:`NvBufSurfaceColorFormat`, Holds the color format of
    the buffer.
    :ivar layout: :class:`NvBufSurfaceLayout`, Holds the surface layout (PL or GL).
    For dGPU,, only PL is valid.
    :ivar bufferDesc: *int*, Holds a DMABUF FD. Valid only for
    NVBUF_MEM_SURFACE_ARRAY and NVBUF_MEM_HANDLE type memory.
    :ivar dataSize: *int*, Holds the amount of allocated memory.
    :ivar dataPtr: Allocated memory. Not valid for NVBUF_MEM_SURFACE_ARRAY or
    NVBUF_MEM_HANDLE.
    :ivar planeParams: :class:`NvBufSurfacePlaneParams`, Holds planewise information
    (width, height, pitch, offset, etc.).
    :ivar mappedAddr: :class:`NvBufSurfaceMappedAddr`, Holds mapped buffers.
    Initialized to None when the structure is created.
    """

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvBufSurfaceParams]) -> NvBufSurfaceParams:
        """Cast given object/data to :class:`NvBufSurfaceParams`,
        call pyds.NvBufSurfaceParams.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvBufSurfaceParams:
        """Cast given object/data to :class:`NvBufSurfaceParams`,
        call pyds.NvBufSurfaceParams.cast(data).
        """

    @property
    def bufferDesc(self) -> int: ...
    @property
    def colorFormat(self) -> NvBufSurfaceColorFormat: ...
    @property
    def dataPtr(self) -> typing.Any: ...
    @property
    def dataSize(self) -> int: ...
    @property
    def height(self) -> int: ...
    @property
    def layout(self) -> NvBufSurfaceLayout: ...
    @property
    def mappedAddr(self) -> NvBufSurfaceMappedAddr: ...
    @property
    def pitch(self) -> int: ...
    @property
    def planeParams(self) -> NvBufSurfacePlaneParams: ...
    @property
    def width(self) -> int: ...

class NvBufSurfacePlaneParams:
    """Holds the planewise parameters of a buffer.

    :ivar num_planes: *int*, Holds the number of planes.
    :ivar width: *list of int*, Holds the widths of planes.
    :ivar height: *list of int*, Holds the heights of planes.
    :ivar pitch: *list of int*, Holds the pitches of planes.
    :ivar offset: *list of int*, Holds the offsets of planes.
    :ivar psize: *list of int*, Holds the sizes of planes.
    :ivar bytesPerPix: *list of int*, Holds the number of bytes occupied by a pixel
    in each plane.
    """

    num_planes: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvBufSurfacePlaneParams]) -> NvBufSurfacePlaneParams:
        """Cast given object/data to :class:`NvBufSurfacePlaneParams`,
        call pyds.NvBufSurfacePlaneParams.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvBufSurfacePlaneParams:
        """Cast given object/data to :class:`NvBufSurfacePlaneParams`,
        call pyds.NvBufSurfacePlaneParams.cast(data).
        """

    @property
    def bytesPerPix(self) -> numpy.ndarray: ...
    @bytesPerPix.setter
    def bytesPerPix(self) -> None: ...
    @property
    def height(self) -> numpy.ndarray: ...
    @height.setter
    def height(self) -> None: ...
    @property
    def offset(self) -> numpy.ndarray: ...
    @offset.setter
    def offset(self) -> None: ...
    @property
    def pitch(self) -> numpy.ndarray: ...
    @pitch.setter
    def pitch(self) -> None: ...
    @property
    def psize(self) -> numpy.ndarray: ...
    @psize.setter
    def psize(self) -> None: ...
    @property
    def width(self) -> numpy.ndarray: ...
    @width.setter
    def width(self) -> None: ...

class NvDsAnalyticsFrameMeta:
    """Holds a set of nvdsanalytics frame level metadata.

    :ivar ocStatus: *dict<str, bool>*, Holds a map of boolean status of overcrowding
    for configured ROIs,which can be accessed using key, value pair; where key is the
    ROI label.
    :ivar objInROIcnt: *dict<str, int>*, Holds a map of total count of valid objects
    in ROI  for configured ROIs,which can be accessed using key, value pair; where
    key is the ROI label.
    :ivar objLCCurrCnt: *dict<str, int>*, Holds a map of total count of Line crossing
    in current frame for configured lines, which can be accessed using key,
    value pair; where key is the line crossing label.
    :ivar objLCCumCnt: *dict<str, int>*, Holds a map of total cumulative count of
    Line crossing  for configured lines, can be accessed using key, value pair; where
    key is the line crossing label
    :ivar unique_id: *str*, Holds unique identifier for nvdsanalytics instance.
    :ivar objCnt: *int*, Holds a map of total count of objects for each class ID,
    can be accessed using key, value pair; where key is class ID.

    Example usage:
    ::

        # Get meta data from NvDsAnalyticsFrameMeta
        l_user = frame_meta.frame_user_meta_list #Get glist containing NvDsUserMeta
        objects from given NvDsFrameMeta
        while l_user:
            try:
                user_meta = pyds.NvDsUserMeta.cast(l_user.data) #Must cast glist data
                to NvDsUserMeta object
                if user_meta.base_meta.meta_type == pyds.nvds_get_user_meta_type(
                "NVIDIA.DSANALYTICSFRAME.USER_META"):
                    user_meta_data = pyds.NvDsAnalyticsFrameMeta.cast(
                    user_meta.user_meta_data) #Must cast user metadata to
                    NvDsAnalyticsFrameMeta
                    #Access NvDsAnalyticsFrameMeta attributes with user_meta_data.{
                    attribute name}
                    if user_meta_data.objInROIcnt: print("Objs in ROI: {0}".format(
                    user_meta_data.objInROIcnt))
                    if user_meta_data.objLCCumCnt: print("Linecrossing Cumulative: {
                    0}".format(user_meta_data.objLCCumCnt))
                    if user_meta_data.objLCCurrCnt: print("Linecrossing Current
                    Frame: {0}".format(user_meta_data.objLCCurrCnt))
                    if user_meta_data.ocStatus: print("Overcrowding status: {
                    0}".format(user_meta_data.ocStatus))
            except StopIteration:
                break
            try:
                l_user = l_user.next
            except StopIteration:
                break
    """

    objCnt: dict[int, int]
    objInROIcnt: dict[str, int]
    objLCCumCnt: dict[str, int]
    objLCCurrCnt: dict[str, int]
    ocStatus: dict[str, bool]
    unique_id: int

    @staticmethod
    def cast(data: capsule[NvDsAnalyticsFrameMeta]) -> NvDsAnalyticsFrameMeta:
        """Cast given object/data to :class:`NvDsAnalyticsFrameMeta`,
        call pyds.NvDsAnalyticsFrameMeta.cast(data).
        """

    def __init__(self) -> None: ...

class NvDsAnalyticsObjInfo:
    """Holds a set of nvdsanalytics object level metadata.

    :ivar roiStatus: *list of str*, Holds the array of ROI labels in which object is
    present.
    :ivar ocStatus: *list of str*, Holds the array  of OverCrowding labels in which
    object is present.
    :ivar lcStatus: *list of str*, Holds the array of line crossing labels which
    object has crossed.
    :ivar dirStatus: *str*, Holds the direction string for the tracked object.
    :ivar unique_id: *int*, Holds unique identifier for nvdsanalytics instance.

    Example usage:
    ::

        # Extract object level meta data from NvDsAnalyticsObjInfo
        l_user_meta = obj_meta.obj_user_meta_list #Get glist containing NvDsUserMeta
        objects from given NvDsObjectMeta
        # Extract object level meta data from NvDsAnalyticsObjInfo
        while l_user_meta:
            try:
                user_meta = pyds.NvDsUserMeta.cast(l_user_meta.data) #Must cast glist
                data to NvDsUserMeta object
                if user_meta.base_meta.meta_type == pyds.nvds_get_user_meta_type(
                "NVIDIA.DSANALYTICSOBJ.USER_META"):
                user_meta_data = pyds.NvDsAnalyticsObjInfo.cast(
                user_meta.user_meta_data) #Must cast user metadata to
                NvDsAnalyticsObjInfo
                #Access NvDsAnalyticsObjInfo attributes with user_meta_data.{
                attribute name}
                if user_meta_data.dirStatus: print("Object {0} moving in direction: {
                1}".format(obj_meta.object_id, user_meta_data.dirStatus))
                if user_meta_data.lcStatus: print("Object {0} line crossing status: {
                1}".format(obj_meta.object_id, user_meta_data.lcStatus))
                if user_meta_data.ocStatus: print("Object {0} overcrowding status: {
                1}".format(obj_meta.object_id, user_meta_data.ocStatus))
                if user_meta_data.roiStatus: print("Object {0} roi status: {
                1}".format(obj_meta.object_id, user_meta_data.roiStatus))
            except StopIteration:
                break

            try:
                l_user_meta = l_user_meta.next
                except StopIteration:
                break
    """

    dirStatus: str
    lcStatus: list[str]
    ocStatus: list[str]
    roiStatus: list[str]
    unique_id: int

    @staticmethod
    def cast(data: capsule[NvDsAnalyticsObjInfo]) -> NvDsAnalyticsObjInfo:
        """Cast given object/data to :class:`NvDsAnalyticsObjInfo`,
        call pyds.NvDsAnalyticsObjInfo.cast(data).
        """

    def __init__(self) -> None: ...

class NvDsBaseMeta:
    """Holds information about base metadata of given metadata type.

    :ivar batch_meta: batch_meta
    :ivar meta_type: Metadata type of the given element.
    :ivar uContext: user context
    """

    batch_meta: NvDsBatchMeta
    meta_type: NvDsMetaType
    uContext: typing.Any

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsBaseMeta]) -> NvDsBaseMeta:
        """Cast given object/data to :class:`NvDsBaseMeta`,
        call pyds.NvDsBaseMeta.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsBaseMeta:
        """Cast given object/data to :class:`NvDsBaseMeta`,
        call pyds.NvDsBaseMeta.cast(data).
        """

class NvDsBatchMeta:
    """Holds information a formed batched containing the frames from different sources.

    NOTE: Both Video and Audio metadata uses the same :class:`NvDsBatchMeta` type.

    NOTE: Audio batch metadata is formed within nvinferaudio plugin and will not be
    corresponding to any one buffer output from nvinferaudio.
    The :class:`NvDsBatchMeta` for audio is attached to the last input buffer when
    the audio batch buffering reach configurable threshold (audio frame length)
    and this is when inference output is available.

    :ivar base_meta: :class:`NvDsBaseMeta`, base_meta
    :ivar max_frames_in_batch: *int*, maximum number of frames those can be present
    the batch.
    :ivar num_frames_in_batch: *int*, Number of frames present in the current batch.
    :ivar frame_meta_pool: :class:`NvDsMetaPool`, pool of type :class:`NvDsFrameMeta`.
    :ivar obj_meta_pool: :class:`NvDsMetaPool`, pool of type :class:`NvDsObjMeta`.
    :ivar classifier_meta_pool: :class:`NvDsMetaPool`, pool of type
    :class:`NvDsClassifierMeta`.
    :ivar display_meta_pool: :class:`NvDsMetaPool`, A pool of type
    :class:`NvDsDisplayMeta`.
    :ivar user_meta_pool: :class:`NvDsMetaPool`, A pool of type :class:`NvDsUserMeta`.
    :ivar label_info_meta_pool: :class:`NvDsMetaPool`, A pool of type
    :class:`NvDsLabelInfo`.
    :ivar frame_meta_list: A list of items of type :class:`NvDsFrameMeta` in use in
    the current batch.
    :ivar batch_user_meta_list: A list of items of type :class:`NvDsUserMeta` in use
    in the current batch.
    :ivar meta_mutex: *GRecMutex*, lock to be taken before accessing metadata to
    avoid simultaneous update of same metadata by multiple components.
    :ivar misc_batch_info: *list of int*, For additional user specific batch info.
    :ivar reserved: *int*, Reserved for internal use.

    Example usage:
    ::

        # Retrieve batch metadata from the gst_buffer
        # Note that pyds.gst_buffer_get_nvds_batch_meta() expects the
        # C address of gst_buffer as input, which is obtained with hash(gst_buffer)
        batch_meta = pyds.gst_buffer_get_nvds_batch_meta(hash(gst_buffer))
        l_frame = batch_meta.frame_meta_list #Get list containing NvDsFrameMeta
        objects from retrieved NvDsBatchMeta
    """

    base_meta: NvDsBaseMeta
    batch_user_meta_list: GList[NvDsUserMeta]
    classifier_meta_pool: NvDsMetaPool
    display_meta_pool: NvDsMetaPool
    frame_meta_list: GList[NvDsFrameMeta]
    frame_meta_pool: NvDsMetaPool
    label_info_meta_pool: NvDsMetaPool
    max_frames_in_batch: int
    meta_mutex: GLib.RecMutex
    num_frames_in_batch: int
    obj_meta_pool: NvDsMetaPool
    user_meta_pool: NvDsMetaPool

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsBatchMeta]) -> NvDsBatchMeta:
        """Cast given object/data to :class:`NvDsBatchMeta`,
        call pyds.NvDsBatchMeta.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsBatchMeta:
        """Cast given object/data to :class:`NvDsBatchMeta`,
        call pyds.NvDsBatchMeta.cast(data).
        """

    @property
    def misc_batch_info(self) -> numpy.ndarray: ...
    @misc_batch_info.setter
    def misc_batch_info(self) -> None: ...
    @property
    def reserved(self) -> numpy.ndarray: ...
    @reserved.setter
    def reserved(self) -> None: ...

class NvDsClassifierMeta:
    """Holds classifier metadata for an object.

    :ivar base_meta: :class:`NvDsBaseMeta`, base_meta
    :ivar num_labels: *int*, Number of outputs/labels of the classifier.
    :ivar unique_component_id: *int*, Unique component id that attaches
    NvDsClassifierMeta metadata.
    :ivar label_info_list: List of objects of type :class:`NvDsLabelInfo`.
    """

    base_meta: NvDsBaseMeta
    label_info_list: GList[NvDsLabelInfo]
    num_labels: int
    unique_component_id: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsClassifierMeta]) -> NvDsClassifierMeta:
        """Cast given object/data to :class:`NvDsClassifierMeta`,
        call pyds.NvDsClassifierMeta.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsClassifierMeta:
        """Cast given object/data to :class:`NvDsClassifierMeta`,
        call pyds.NvDsClassifierMeta.cast(data).
        """

class NvDsComp_BboxInfo:
    """Holds unclipped positional bounding box coordinates of the object processed by
    the component.

    :ivar org_bbox_coords: :class:`NvBbox_Coords`, org_bbox_coords
    """

    org_bbox_coords: NvBbox_Coords

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsComp_BboxInfo]) -> NvDsComp_BboxInfo:
        """Cast given object/data to :class:`NvDsComp_BboxInfo`,
        call pyds.NvDsComp_BboxInfo.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsComp_BboxInfo:
        """Cast given object/data to :class:`NvDsComp_BboxInfo`,
        call pyds.NvDsComp_BboxInfo.cast(data).
        """

class NvDsCoordinate:
    """Hold coordinate parameters.

    :ivar x: *float*, Holds the coordinate's X position.
    :ivar y: *float*, Holds the coordinate's Y position.
    :ivar z: *float*, Holds the coordinate's Z position.
    """

    x: float
    y: float
    z: float

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsCoordinate]) -> NvDsCoordinate:
        """Cast given object/data to :class:`NvDsCoordinate`,
        call pyds.NvDsCoordinate.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsCoordinate:
        """Cast given object/data to :class:`NvDsCoordinate`,
        call pyds.NvDsCoordinate.cast(data).
        """

class NvDsDisplayMeta:
    """Holds information of display metadata that user can specify in the frame.

    :ivar base_meta: :class:`NvDsBaseMeta`, base_meta
    :ivar num_rects: *int*, Number of rectangles present in display meta.
    :ivar num_labels: *int*, Number of labels/strings present in display meta.
    :ivar num_lines: *int*, Number of lines present in display meta.
    :ivar rect_params: List of :class:`NvOSD_RectParams`, Holds a list of positional
    parameters for rectangles. Used to overlay borders or semi-transparent
    rectangles, as required by the application. See :class:`NvOSD_RectParams`.
    :ivar text_params: List of :class:`NvOSD_TextParams`, Holds a list of text
    parameters for user-defined strings that can be overlayed using this structure.
    See :class:`NvOSD_TextParams`.
    :ivar line_params: List of :class:`NvOSD_LineParams`, Holds a list of line
    parameters that the user can use to draw polygons in the frame, e.g. to show a
    RoI in the frame. See :class:`NvOSD_LineParams`.
    :ivar num_arrows: *int*, Holds the number of arrows described.
    :ivar num_circles: *int*, Holds the number of circles described.
    :ivar arrow_params: List of :class:`NvOSD_ArrowParams`, Holds a list of arrow
    parameters that the user can use to draw arrows in the frame. See
    :class:`NvOSD_ArrowParams`:
    :ivar circle_params: List of :class:`NvOSD_CircleParams`, Holds a list of circle
    parameters that the user can use to draw circle in the frame. See
    :class:`NvOSD_CircleParams`.
    :ivar misc_osd_data: *np.array of int*, Holds an np.array of user-defined OSD
    metadata.
    :ivar reserved: *list of int*, Reserved for internal use.

    Example usage:
    ::

        display_meta=pyds.nvds_acquire_display_meta_from_pool(batch_meta) #Retrieve
        NvDsDisplayMeta object from pool in given NvDsBatchMeta object
        display_meta.num_labels = 1
        py_nvosd_text_params = display_meta.text_params[0] #Retrieve NvOSD_TextParams
        object from list in display meta. See NvOSD docs for more details.
        # Setting display text to be shown on screen
        # Note that the pyds module allocates a buffer for the string, and the
        # memory will not be claimed by the garbage collector.
        # Reading the display_text field here will return the C address of the
        # allocated string. Use pyds.get_string() to get the string content.
        py_nvosd_text_params.display_text = "Frame Number={} Number of Objects={}
        Vehicle_count={} Person_count={}".format(frame_number, num_rects,
        obj_counter[PGIE_CLASS_ID_VEHICLE], obj_counter[PGIE_CLASS_ID_PERSON])

        print(pyds.get_string(py_nvosd_text_params.display_text))
        pyds.nvds_add_display_meta_to_frame(frame_meta, display_meta) #Use method to
        add display_meta to frame_meta.
    """

    base_meta: NvDsBaseMeta
    num_arrows: int
    num_circles: int
    num_labels: int
    num_lines: int
    num_rects: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsDisplayMeta]) -> NvDsDisplayMeta:
        """Cast given object/data to :class:`NvDsDisplayMeta`,
        call pyds.NvDsDisplayMeta.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsDisplayMeta:
        """Cast given object/data to :class:`NvDsDisplayMeta`,
        call pyds.NvDsDisplayMeta.cast(data).
        """

    @property
    def arrow_params(self) -> list[NvOSD_ArrowParams]: ...
    @property
    def circle_params(self) -> list[NvOSD_CircleParams]: ...
    @property
    def line_params(self) -> list[NvOSD_LineParams]: ...
    @property
    def misc_osd_data(self) -> numpy.ndarray: ...
    @misc_osd_data.setter
    def misc_osd_data(self) -> None: ...
    @property
    def rect_params(self) -> list[NvOSD_RectParams]: ...
    @property
    def reserved(self) -> numpy.ndarray: ...
    @reserved.setter
    def reserved(self) -> None: ...
    @property
    def text_params(self) -> list[NvOSD_TextParams]: ...

class NvDsEvent:
    """Holds event information.

    :ivar eventType: :class:`NvDsEventType`, Type of event.
    :ivar metadata: :class:`NvDsEventMsgMeta`, object of event meta data.
    """

    eventType: NvDsEventType
    metadata: NvDsEventMsgMeta

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsEvent]) -> NvDsEvent:
        """Cast given object/data to :class:`NvDsEvent`, call pyds.NvDsEvent.cast(
        data).
        """

    @typing.overload
    def cast(self: int) -> NvDsEvent:
        """Cast given object/data to :class:`NvDsEvent`, call pyds.NvDsEvent.cast(
        data).
        """

class NvDsEventMsgMeta:
    r"""Holds event message meta data. You can attach various types of objects (
    vehicle, person, face, etc.) to an event by setting a pointer to the object in
    :py:attr:`extMsg`.
    Similarly, you can attach a custom object to an event by setting a pointer to the
    object in :py:attr:`extMsg`.
    A custom object must be handled by the metadata parsing module accordingly.

    :ivar type: :class:`NvDsEventType`, Type of event.
    :ivar objType: :class:`NvDsObjectType`, Type of object.
    :ivar bbox: :class:`NvDsRect`, Bounding box of object.
    :ivar location: :class:`NvDsGeoLocation`, Geo-location of object.
    :ivar coordinate: :class:`NvDsCoordinate`, Coordinate of object.
    :ivar objSignature: :class:`NvDsObjectSignature`, Signature of object.
    :ivar objClassId: *int*, Class id of object.
    :ivar sensorId: *int*, ID of sensor that generated the event.
    :ivar moduleId: *int*, ID of analytics module that generated the event.
    :ivar placeId: *int*, ID of place related to the object.
    :ivar componentId: *int*, ID of component that generated this event.
    :ivar frameId: *int*, Video frame ID of this event.
    :ivar confidence: *int*, Confidence level of the inference.
    :ivar trackingId: *int*, Tracking ID of object.
    :ivar ts: *str*, Time stamp of generated event.
    :ivar objectId: *str*, ID of detected / inferred object.
    :ivar sensorStr: *str*, Identity string of sensor.
    :ivar otherAttrs: *str*, Other attributes associated with the object.
    :ivar videoPath: *str*, Name of video file.
    :ivar extMsg: Object to extend the event message meta data. This can be used for
    custom values that can't be accommodated in the existing fields
        OR if object(vehicle, person, face etc.) Specific values must be attached.
    :ivar extMsgSize: *int*, Size of the custom object at extMsg.

    Example usage:
    ::

        def generate_event_msg_meta(data, class_id):
            meta =pyds.NvDsEventMsgMeta.cast(data)
            meta.sensorId = 0
            meta.placeId = 0
            meta.moduleId = 0
            meta.sensorStr = "sensor-0"
            meta.ts = pyds.alloc_buffer(MAX_TIME_STAMP_LEN + 1)
            pyds.generate_ts_rfc3339(meta.ts, MAX_TIME_STAMP_LEN) #Generate timestamp

            # This demonstrates how to attach custom objects.
            # Any custom object as per requirement can be generated and attached
            # like NvDsVehicleObject / NvDsPersonObject. Then that object should
            # be handled in payload generator library (nvmsgconv.cpp) accordingly.
            if(class_id==PGIE_CLASS_ID_VEHICLE):
                meta.type = pyds.NvDsEventType.NVDS_EVENT_MOVING
                meta.objType = pyds.NvDsObjectType.NVDS_OBJECT_TYPE_VEHICLE
                meta.objClassId = PGIE_CLASS_ID_VEHICLE
                obj = pyds.alloc_nvds_vehicle_object()
                obj = generate_vehicle_meta(obj) #See NvDsVehicleObject example code
                meta.extMsg = obj
                meta.extMsgSize = sys.getsizeof(pyds.NvDsVehicleObject);
            if(class_id == PGIE_CLASS_ID_PERSON):
                meta.type =pyds.NvDsEventType.NVDS_EVENT_ENTRY
                meta.objType = pyds.NvDsObjectType.NVDS_OBJECT_TYPE_PERSON;
                meta.objClassId = PGIE_CLASS_ID_PERSON
                obj = pyds.alloc_nvds_person_object()
                obj=generate_person_meta(obj)
                meta.extMsg = obj
                meta.extMsgSize = sys.getsizeof(pyds.NvDsPersonObject)
            return meta

        ...

        # Allocating an NvDsEventMsgMeta instance and getting reference
        # to it. The underlying memory is not manged by Python so that
        # downstream plugins can access it. Otherwise the garbage collector
        # will free it when this probe exits.
        msg_meta=pyds.alloc_nvds_event_msg_meta()
        msg_meta.bbox.top =  obj_meta.rect_params.top
        msg_meta.bbox.left =  obj_meta.rect_params.left
        msg_meta.bbox.width = obj_meta.rect_params.width
        msg_meta.bbox.height = obj_meta.rect_params.height
        msg_meta.frameId = frame_number
        msg_meta.trackingId = long_to_uint64(obj_meta.object_id)
        msg_meta.confidence = obj_meta.confidence
        msg_meta = generate_event_msg_meta(msg_meta, obj_meta.class_id)
        user_event_meta = pyds.nvds_acquire_user_meta_from_pool(batch_meta)
        if(user_event_meta):
            user_event_meta.user_meta_data = msg_meta;
            user_event_meta.base_meta.meta_type = pyds.NvDsMetaType.NVDS_EVENT_MSG_META
            # Setting callbacks in the event msg meta. The bindings layer
            # will wrap these callables in C functions. Currently only one
            # set of callbacks is supported.
            pyds.user_copyfunc(user_event_meta, meta_copy_func)
            pyds.user_releasefunc(user_event_meta, meta_free_func)
            pyds.nvds_add_user_meta_to_frame(frame_meta, user_event_meta)
        else:
            print("Error in attaching event meta to buffer\\n")
    """

    bbox: NvDsRect
    componentId: int
    confidence: float
    coordinate: NvDsCoordinate
    extMsg: typing.Any
    extMsgSize: int
    frameId: int
    location: NvDsGeoLocation
    moduleId: int
    objClassId: int
    objSignature: NvDsObjectSignature
    objType: NvDsObjectType
    placeId: int
    sensorId: int
    trackingId: int
    ts: int
    type: NvDsEventType

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsEventMsgMeta]) -> NvDsEventMsgMeta:
        """Casts to :class:`NvDsEventMsgMeta` object, call pyds.NvDsEventMsgMeta(
        data).
        """

    @typing.overload
    def cast(self: int) -> NvDsEventMsgMeta:
        """Casts to :class:`NvDsEventMsgMeta` object, call pyds.NvDsEventMsgMeta(
        data).
        """

    @property
    def objectId(self) -> int: ...
    @objectId.setter
    def objectId(self, arg1: str) -> None: ...
    @property
    def otherAttrs(self) -> int: ...
    @otherAttrs.setter
    def otherAttrs(self, arg1: str) -> None: ...
    @property
    def sensorStr(self) -> int: ...
    @sensorStr.setter
    def sensorStr(self, arg1: str) -> None: ...
    @property
    def videoPath(self) -> int: ...
    @videoPath.setter
    def videoPath(self, arg1: str) -> None: ...

class NvDsEventType:
    """*Enumerator*. Event type flags.

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

      NVDS_EVENT_CUSTOM : Specifies a custom event.

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
    # 'NVDS_EVENT_EXIT': NvDsEventType.NVDS_EVENT_EXIT, 'NVDS_EVENT_MOVING':
    # NvDsEventType.NVDS_EVENT_MOVING, 'NVDS_EVENT_STOPPED':
    # NvDsEventType.NVDS_EVENT_STOPPED, 'NVDS_EVENT_EMPTY':
    # NvDsEventType.NVDS_EVENT_EMPTY, 'NVDS_EVENT_PARKED':
    # NvDsEventType.NVDS_EVENT_PARKED, 'NVDS_EVENT_RESET':
    # NvDsEventType.NVDS_EVENT_RESET, 'NVDS_EVENT_RESERVED':
    # NvDsEventType.NVDS_EVENT_RESERVED, 'NVDS_EVENT_CUSTOM':
    # NvDsEventType.NVDS_EVENT_CUSTOM, 'NVDS_EVENT_FORCE32':
    # NvDsEventType.NVDS_EVENT_FORCE32}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str."""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvDsEventType, arg0: int) -> None."""

    def __index__(self) -> int: ...
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...

class NvDsFaceObject:
    """Holds face parameters.

    :ivar gender: *str*, Person's gender.
    :ivar hair: *str*, Person's hair color.
    :ivar cap: *str*, Type of cap the person is wearing, if any.
    :ivar glasses: *str*, Type of glasses the person is wearing, if any.
    :ivar facialhair: *str*, Person's facial hair color.
    :ivar name: *str*, Person's name.
    :ivar eyecolor: *str*, Person's eye color.
    :ivar age: *int*, Person's age.
    """

    age: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsFaceObject]) -> NvDsFaceObject:
        """Casts to :class:`NvDsFaceObject` object, call pyds.NvDsFaceObject(data)."""

    @typing.overload
    def cast(self: int) -> NvDsFaceObject:
        """Casts to :class:`NvDsFaceObject` object, call pyds.NvDsFaceObject(data)."""

    @property
    def cap(self) -> int: ...
    @cap.setter
    def cap(self, arg1: str) -> None: ...
    @property
    def eyecolor(self) -> int: ...
    @eyecolor.setter
    def eyecolor(self, arg1: str) -> None: ...
    @property
    def facialhair(self) -> int: ...
    @facialhair.setter
    def facialhair(self, arg1: str) -> None: ...
    @property
    def gender(self) -> int: ...
    @gender.setter
    def gender(self, arg1: str) -> None: ...
    @property
    def glasses(self) -> int: ...
    @glasses.setter
    def glasses(self, arg1: str) -> None: ...
    @property
    def hair(self) -> int: ...
    @hair.setter
    def hair(self, arg1: str) -> None: ...
    @property
    def name(self) -> int: ...
    @name.setter
    def name(self, arg1: str) -> None: ...

class NvDsFaceObjectWithExt:
    """Holds a vehicle object's parameters.

    :ivar gender: *str*, Person's gender.
    :ivar hair: *str*, Person's hair color.
    :ivar cap: *str*, Type of cap the person is wearing, if any.
    :ivar glasses: *str*, Type of glasses the person is wearing, if any.W
    :ivar facialhair: *str*, Person's facial hair color.Ws
    :ivar name: *str*, Person's name.
    :ivar eyecolor: *str*, Person's eye color.
    :ivar age: *int*, Person's age.
    :ivar mask: *Glist* of polygons for face mask.
    """

    age: int
    cap: str
    eyecolor: str
    facialhair: str
    gender: str
    glasses: str
    hair: str
    mask: GList[typing.Any]
    name: str

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsFaceObjectWithExt]) -> NvDsFaceObjectWithExt:
        """Cast given object/data to :class:`NvDsFaceObjectWithExt`,
        call pyds.NvDsFaceObjectWithExt.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsFaceObjectWithExt:
        """Cast given object/data to :class:`NvDsFaceObjectWithExt`,
        call pyds.NvDsFaceObjectWithExt.cast(data).
        """

class NvDsFrameMeta:
    """Holds metadata for a frame in a batch.

    :ivar base_meta: :class:`NvDsBaseMeta`, Base metadata for frame.
    :ivar pad_index: *int*, Pad or port index of stream muxer component for the frame
    in the batch.
    :ivar batch_id: *int*, Location of the frame in the batch.
    :class:`NvBufSurfaceParams` for the frame will be at index batch_id in the
    surfaceList array of :class:`NvBufSurface`.
    :ivar frame_num: *int*, Current frame number of the source.
    :ivar buf_pts: *int*, Holds the presentation timestamp (PTS) of the frame.
    :ivar ntp_timestamp: *int*, Holds the ntp (network time protocol) timestamp.
    :ivar source_id: *int*, Source_id of the frame in the batch e.g. camera_id. It
    need not be in sequential order.
    :ivar num_surfaces_per_frame: *int*, Number of surfaces present in this frame.
    This is required in case multiple surfaces per frame.
    :ivar source_frame_width: *int*, Holds the width of the frame at input to
    Gst-streammux.
    :ivar source_frame_height: *int*, Holds the height of the frame at input to
    Gst-streammux.
    :ivar surface_type: *int*, Surface type of sub frame. This is required in case
    multiple surfaces per frame.
    :ivar surface_index: *int*, Surface index of sub frame. This is required in case
    multiple surfaces per frame.
    :ivar num_obj_meta: *int*, Number of object meta elements attached to the current
    frame.
    :ivar bInferDone: *int*, Boolean indicating whether inference is performed on
    given frame.
    :ivar obj_meta_list: List of objects of type :class:`NvDsObjectMeta` in use for
    the given frame.
    :ivar display_meta_list: List of objects of type :class:`NvDsDisplayMeta` in use
    for the given frame.
    :ivar frame_user_meta_list: List of objects of type :class:`NvDsUserMeta` in use
    for the given frame.
    :ivar misc_frame_info: *list of int*, For additional user specific batch info.
    :ivar reserved: *int*, Reserved for internal use.

    Example usage:
    ::

        batch_meta = pyds.gst_buffer_get_nvds_batch_meta(hash(gst_buffer)) #Retrieve
        batch metadata from gst_buffer
        l_frame = batch_meta.frame_meta_list
        while l_frame is not None:
            try:
                frame_meta = pyds.NvDsFrameMeta.cast(l_frame.data) #Must cast data in
                frame_meta_list to NvDsFrameMeta object
            except StopIteration:
                break

            frame_number=frame_meta.frame_num #Retrieve current frame number from
            NvDsFrameMeta object
            num_rects = frame_meta.num_obj_meta #Retrieve number of objects in frame
            from NvDsFrameMeta object
            l_obj=frame_meta.obj_meta_list #Retrieve list of NvDsObjectMeta objects
            in frame from NvDsFrameMeta object
    """

    bInferDone: int
    base_meta: NvDsBaseMeta
    batch_id: int
    buf_pts: int
    display_meta_list: GList[NvDsDisplayMeta]
    frame_num: int
    frame_user_meta_list: GList[NvDsUserMeta]
    ntp_timestamp: int
    num_obj_meta: int
    num_surfaces_per_frame: int
    obj_meta_list: GList[NvDsObjectMeta]
    pad_index: int
    source_frame_height: int
    source_frame_width: int
    source_id: int
    surface_index: int
    surface_type: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsFrameMeta]) -> NvDsFrameMeta:
        """Cast given object/data to :class:`NvDsFrameMeta`,
        call pyds.NvDsFrameMeta.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsFrameMeta:
        """Cast given object/data to :class:`NvDsFrameMeta`,
        call pyds.NvDsFrameMeta.cast(data).
        """

    @property
    def misc_frame_info(self) -> numpy.ndarray: ...
    @misc_frame_info.setter
    def misc_frame_info(self) -> None: ...
    @property
    def reserved(self) -> numpy.ndarray: ...
    @reserved.setter
    def reserved(self) -> None: ...

class NvDsGeoLocation:
    """Holds Geo-location parameters.

    :ivar lat: *float*, Holds the location's latitude.
    :ivar lon: *float*, Holds the location's longitude.
    :ivar alt: *float*, Holds the location's altitude.
    """

    alt: float
    lat: float
    lon: float

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsGeoLocation]) -> NvDsGeoLocation:
        """Cast given object/data to :class:`NvDsGeoLocation`,
        call pyds.NvDsGeoLocation.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsGeoLocation:
        """Cast given object/data to :class:`NvDsGeoLocation`,
        call pyds.NvDsGeoLocation.cast(data).
        """

class NvDsInferAttribute:
    """Holds information about one classified attribute.

    :ivar atttributeIndex: *int*, Index of the label. This index corresponds to the
    order of output layers specified in the outputCoverageLayerNames vector during
    initialization. WARNING: misspelling to be deprecated, please change all usage to
    "attributeIndex".
    :ivar attributeIndex: *int*, Index of the label. This index corresponds to the
    order of output layers specified in the outputCoverageLayerNames vector during
    initialization.
    :ivar attributeValue: *int*, Output for the label.
    :ivar attributeConfidence: *float*, Confidence level for the classified attribute.
    :ivar attributeLabel: *str*, String label for the attribute. Memory for the
    string should not be freed.
    """

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsInferAttribute]) -> NvDsInferAttribute:
        """Cast given object/data to :class:`NvDsInferObjectDetectionInfo`,
        call pyds.NvDsInferObjectDetectionInfo.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsInferAttribute:
        """Cast given object/data to :class:`NvDsInferObjectDetectionInfo`,
        call pyds.NvDsInferObjectDetectionInfo.cast(data).
        """

    @property
    def attributeConfidence(self) -> float: ...
    @property
    def attributeIndex(self) -> int: ...
    @property
    def attributeLabel(self) -> str: ...
    @property
    def attributeValue(self) -> int: ...
    @property
    def atttributeIndex(self) -> int: ...

class NvDsInferDataType:
    """*Enumerator*, Specifies the data type of a layer.

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
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str."""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvDsInferDataType, arg0: int) -> None."""

    def __index__(self) -> int: ...
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...

class NvDsInferDims:
    """Specifies dimensions of a layer.

    :ivar numDims: *int*, Number of dimesions of the layer.
    :ivar numElements: *int*, Number of elements in the layer including all dimensions.
    :ivar d: *np.array of int*, Size of the layer in each dimension.
    """

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsInferDims]) -> NvDsInferDims:
        """Cast given object/data to :class:`NvDsInferDims`,
        call pyds.NvDsInferDims.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsInferDims:
        """Cast given object/data to :class:`NvDsInferDims`,
        call pyds.NvDsInferDims.cast(data).
        """

    @property
    def d(self) -> numpy.ndarray: ...
    @d.setter
    def d(self) -> None: ...
    @property
    def numDims(self) -> int: ...
    @property
    def numElements(self) -> int: ...

class NvDsInferDimsCHW:
    """Holds the dimensions of a three-dimensional layer.

    :ivar c: *int*, Channel count of the layer.
    :ivar h: *int*, Height of the layer.
    :ivar w: *int*, Width of the layer.
    """

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsInferDimsCHW]) -> NvDsInferDimsCHW:
        """Cast given object/data to :class:`NvDsInferDimsCHW`,
        call pyds.NvDsInferDimsCHW.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsInferDimsCHW:
        """Cast given object/data to :class:`NvDsInferDimsCHW`,
        call pyds.NvDsInferDimsCHW.cast(data).
        """

    @property
    def c(self) -> int: ...
    @property
    def h(self) -> int: ...
    @property
    def w(self) -> int: ...

class NvDsInferLayerInfo:
    """Holds information about one layer in the model.

    :ivar dataType: :class:`NvDsInferDataType`, Data type of the layer.
    :ivar dims: :class:`NvDsInferDims`, Dimensions of the layer. WARNING: to be
    deprecated, please change all usage to "inferDims".
    :ivar inferDims: :class:`NvDsInferDims`, Dimensions of the layer.
    :ivar bindingIndex: *int*, TensorRT binding index of the layer.
    :ivar layerName: *str*, Name of the layer.
    :ivar buffer: Buffer for the layer data.
    :ivar isInput: *int*, Holds a Boolean; true if the layer is an input layer,
    or false (0) if an output layer.
    """

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsInferLayerInfo]) -> NvDsInferLayerInfo:
        """Cast given object/data to :class:`NvDsInferLayerInfo`,
        call pyds.NvDsInferLayerInfo.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsInferLayerInfo:
        """Cast given object/data to :class:`NvDsInferLayerInfo`,
        call pyds.NvDsInferLayerInfo.cast(data).
        """

    @property
    def bindingIndex(self) -> int: ...
    @property
    def buffer(self) -> typing.Any: ...
    @property
    def dataType(self) -> NvDsInferDataType: ...
    @property
    def dims(self) -> NvDsInferDims: ...
    @property
    def inferDims(self) -> NvDsInferDims: ...
    @property
    def isInput(self) -> int: ...
    @property
    def layerName(self) -> str: ...

class NvDsInferNetworkInfo:
    """Holds information about the model network.

    :ivar width: *int*, Input width for the model.
    :ivar height: *int*, Input height for the model.
    :ivar channels: *int*, Number of input channels for the model.
    """

    channels: int
    height: int
    width: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsInferNetworkInfo]) -> NvDsInferNetworkInfo:
        """Cast given object/data to :class:`NvDsInferNetworkInfo`,
        call pyds.NvDsInferNetworkInfo.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsInferNetworkInfo:
        """Cast given object/data to :class:`NvDsInferNetworkInfo`,
        call pyds.NvDsInferNetworkInfo.cast(data).
        """

class NvDsInferObjectDetectionInfo:
    """Holds information about one parsed object from detector's output.

    :ivar classId: *int*, ID of the class to which the object belongs.
    :ivar left: *float*, Horizontal offset of the bounding box shape for the object.
    :ivar top: *float*, Vertical offset of the bounding box shape for the object.
    :ivar width: *float*, Width of the bounding box shape for the object.
    :ivar height: *float*, Height of the bounding box shape for the object.
    :ivar detectionConfidence: *float*, Object detection confidence. Should be a
            float value in the range [0.0,1.0].
    """

    classId: int
    detectionConfidence: float
    height: float
    left: float
    top: float
    width: float

    def __init__(self) -> None: ...
    @typing.overload
    def cast(
        self: capsule[NvDsInferObjectDetectionInfo],
    ) -> NvDsInferObjectDetectionInfo:
        """Cast given object/data to :class:`NvDsInferObjectDetectionInfo`,
        call pyds.NvDsInferObjectDetectionInfo.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsInferObjectDetectionInfo:
        """Cast given object/data to :class:`NvDsInferObjectDetectionInfo`,
        call pyds.NvDsInferObjectDetectionInfo.cast(data).
        """

class NvDsInferSegmentationMeta:
    r"""Holds the segmentation model output information for one frame / one object.
    The "nvinfer" plugins adds this meta for segmentation models.
    This meta data is added as NvDsUserMeta to the frame_user_meta_list of the
    corresponding frame_meta or object_user_meta_list of the corresponding object
    with the meta_type set to NVDSINFER_SEGMENTATION_META. Get mask data using
    :py:func:`get_segmentation_masks`.

    :ivar classes: *int*, Number of classes in the segmentation output.
    :ivar width: *int*, Width of the segmentation output class map.
    :ivar height: *int*, Height of the segmentation output class map.
    :ivar class_map: Array for 2D pixel class map. The output for pixel (x,y)  will
    be at index (y * width + x).
    :ivar class_probabilities_map: The raw array containing the probabilities. The
    probability for class c and pixel (x,y) will be at index (c * width * height + y
    * width + x).
    :ivar priv_data: Private data used for the meta producer's internal memory
    management.

    Example usage:
    ::

        def map_mask_as_display_bgr(mask):
            \"\"\" Assigning multiple colors as image output using the information
                contained in mask. (BGR is opencv standard.)
            \"\"\"
            # getting a list of available classes
            m_list = list(set(mask.flatten()))

            shp = mask.shape
            bgr = np.zeros((shp[0], shp[1], 3))
            for idx in m_list:
                bgr[mask == idx] = COLORS[idx]
            return bgr

        ...

        l_user = frame_meta.frame_user_meta_list #Get glist containing NvDsUserMeta
        objects from given NvDsFrameMeta
        while l_user is not None:
            try:
                # Note that l_user.data needs a cast to pyds.NvDsUserMeta
                # The casting is done by pyds.NvDsUserMeta.cast()
                # The casting also keeps ownership of the underlying memory
                # in the C code, so the Python garbage collector will leave
                # it alone.
                seg_user_meta = pyds.NvDsUserMeta.cast(l_user.data)
            except StopIteration:
                break
            if seg_user_meta and seg_user_meta.base_meta.meta_type == \\
                                pyds.NVDSINFER_SEGMENTATION_META:
                try:
                    # Note that seg_user_meta.user_meta_data needs a cast to
                    # pyds.NvDsInferSegmentationMeta
                    # The casting is done by pyds.NvDsInferSegmentationMeta.cast()
                    # The casting also keeps ownership of the underlying memory
                    # in the C code, so the Python garbage collector will leave
                    # it alone.
                    segmeta = pyds.NvDsInferSegmentationMeta.cast(
                    seg_user_meta.user_meta_data)
                except StopIteration:
                    break
                # Retrieve mask data in the numpy format from segmeta
                # Note that pyds.get_segmentation_masks() expects object of
                # type NvDsInferSegmentationMeta
                masks = pyds.get_segmentation_masks(segmeta)
                masks = np.array(masks, copy=True, order='C')
                # map the obtained masks to colors of 2 classes.
                frame_image = map_mask_as_display_bgr(masks)
                cv2.imwrite(folder_name + "/" + str(frame_number) + ".jpg", frame_image)
            try:
                l_user = l_user.next
            except StopIteration:
                break
    """

    def __init__(self) -> None: ...
    def cast(self: capsule[NvDsInferSegmentationMeta]) -> NvDsInferSegmentationMeta:
        """Cast given object/data to :class:`NvDsInferSegmentationMeta`,
        call pyds.NvDsInferSegmentationMeta.cast(data).
        """

    @property
    def class_map(self) -> int: ...
    @property
    def class_probabilities_map(self) -> float: ...
    @property
    def classes(self) -> int: ...
    @property
    def height(self) -> int: ...
    @property
    def priv_data(self) -> typing.Any: ...
    @property
    def width(self) -> int: ...

class NvDsInferTensorMeta:
    """Holds the raw tensor output information for one frame / one object.
    The "nvinfer" plugins adds this meta when the "output-tensor-meta" property  of
    the element instance is set to TRUE.
    This meta data is added as NvDsUserMeta to the frame_user_meta_list of the
    corresponding frame_meta or object_user_meta_list of the corresponding object
    with the meta_type set to NVDSINFER_TENSOR_OUTPUT_META.

    :ivar unique_id: *int*, Unique ID of the gst-nvinfer instance which attached this
    meta.
    :ivar num_output_layers: *int*, Number of bound output layers.
    :ivar out_buf_ptrs_host: Array of output host buffers for the frame / object.
    :ivar out_buf_ptrs_dev: Array of output device buffers for the frame / object.
    :ivar gpu_id: *int*, GPU device ID on which the device buffers have been allocated.
    :ivar priv_data: Private data used for the meta producer's internal memory
    management.
    """

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsInferTensorMeta]) -> NvDsInferTensorMeta:
        """Cast given object/data to :class:`NvDsInferTensorMeta`,
        call pyds.NvDsInferTensorMeta.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsInferTensorMeta:
        """Cast given object/data to :class:`NvDsInferTensorMeta`,
        call pyds.NvDsInferTensorMeta.cast(data).
        """

    def output_layers_info(self, j: int) -> NvDsInferLayerInfo:
        """Retrieve the :class:`NvDsInferLayerInfo` object of layer at index j."""

    @property
    def gpu_id(self) -> int: ...
    @property
    def network_info(self) -> NvDsInferNetworkInfo: ...
    @property
    def num_output_layers(self) -> int: ...
    @property
    def out_buf_ptrs_dev(self) -> typing.Any: ...
    @property
    def out_buf_ptrs_host(self) -> typing.Any: ...
    @property
    def priv_data(self) -> typing.Any: ...
    @property
    def unique_id(self) -> int: ...

class NvDsLabelInfo:
    """Holds information of label metadata in the classifier.

       :ivar base_meta: :class:`NvDsBaseMeta`, base_meta
       :ivar num_classes: *int*, Number of classes of the given label.
       :ivar result_label: An array to store the string describing the label of the
       classified object.
       :ivar pResult_label: *str*, An object to store the result label if it exceeds
       MAX_LABEL_SIZE bytes.
       :ivar result_class_id: *int*, class_id of the best result.
       :ivar label_id: *int*, Holds the label ID in case there are multiple label
    classifiers.
       :ivar result_prob: *float*, Probability of best result.
    """

    base_meta: NvDsBaseMeta
    label_id: int
    num_classes: int
    pResult_label: str
    result_class_id: int
    result_label: str
    result_prob: float

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsLabelInfo]) -> NvDsLabelInfo:
        """Cast given object/data to :class:`NvDsLabelInfo`,
        call pyds.NvDsLabelInfo.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsLabelInfo:
        """Cast given object/data to :class:`NvDsLabelInfo`,
        call pyds.NvDsLabelInfo.cast(data).
        """

class NvDsMeta:
    """Holds DeepStream meta data.

    :ivar meta: *GstMeta* object.
    :ivar meta_data: Metadata object. Must be cast to another structure based on
    :py:attr:`meta_type`.
    :ivar user_data: User-specific data
    :ivar meta_type: Type of metadata, one of values of :class:`GstNvDsMetaType`
    """

    meta: Gst.Meta
    meta_data: typing.Any
    meta_type: int
    user_data: typing.Any

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsMeta]) -> NvDsMeta:
        """Cast given object/data to :class:`NvDsMeta`, call pyds.NvDsMeta.cast(
        data).
        """

    @typing.overload
    def cast(self: int) -> NvDsMeta:
        """Cast given object/data to :class:`NvDsMeta`, call pyds.NvDsMeta.cast(
        data).
        """

NvDsMetaList: typing.TypeAlias = GList[NvDsMeta]

class NvDsMetaPool:
    """Holds information about given metadata pool.

    :ivar meta_type: :class:`NvDsMetaType`, type of the pool. Used for internal purpose.
    :ivar max_elements_in_pool: *int*, max elements in the pool. Used for internal
    purpose.
    :ivar element_size: *int*, size of an element in the given pool. Used for
    internal purpose.
    :ivar num_empty_elements: *int*, number of empty elements. Used for internal
    purpose.
    :ivar num_full_elements: *int*, number of filled elements. These many elemnts are
    in use.
    :ivar empty_list: :class:`NvDsMetaList`, List containing empty elements.
    :ivar full_list: :class:`NvDsMetaList`, List containing full elements.
    """

    element_size: int
    empty_list: NvDsMetaList
    full_list: NvDsMetaList
    max_elements_in_pool: int
    meta_type: NvDsMetaType
    num_empty_elements: int
    num_full_elements: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsMetaPool]) -> NvDsMetaPool:
        """Cast given object/data to :class:`NvDsMetaPool`,
        call pyds.NvDsMetaPool.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsMetaPool:
        """Cast given object/data to :class:`NvDsMetaPool`,
        call pyds.NvDsMetaPool.cast(data).
        """

class NvDsMetaType:
    """*Enumerator*. Specifies the type of meta data.
                    NVIDIA defined NvDsMetaType will be present in the range from
                    NVDS_BATCH_META to NVDS_START_USER_META.
                    User can add its own metadata type NVDS_START_USER_META onwards.

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

      NVDSINFER_TENSOR_OUTPUT_META : metadata type of raw inference output attached
      by gst-nvinfer. Refer :class:`NvDsInferTensorMeta` for details.

      NVDSINFER_SEGMENTATION_META : metadata type of segmentation model output
      attached by gst-nvinfer. Refer :class:`NvDsInferSegmentationMeta` for details.

      NVDS_CROP_IMAGE_META : Specifies metadata type for JPEG-encoded object
      crops.See the deepstream-image-meta-test app for details.

      NVDS_TRACKER_PAST_FRAME_META : metadata type to be set for tracking previous
      frames

      NVDS_AUDIO_BATCH_META : Specifies metadata type for formed audio batch.

      NVDS_AUDIO_FRAME_META : Specifies metadata type for audio frame.

      NVDS_RESERVED_META : Reserved field

      NVDS_GST_CUSTOM_META : metadata type to be set for metadata attached by nvidia
      gstreamer plugins before nvstreammux gstreamer plugin. It is set as user
      metadata inside :class:`NvDsFrameMeta`. NVIDIA specific gst meta are in the
      range from NVDS_GST_CUSTOM_META to NVDS_GST_CUSTOM_META + 4096

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
    # 'NVDS_BATCH_META': NvDsMetaType.NVDS_BATCH_META, 'NVDS_FRAME_META':
    # NvDsMetaType.NVDS_FRAME_META, 'NVDS_OBJ_META': NvDsMetaType.NVDS_OBJ_META,
    # 'NVDS_DISPLAY_META': NvDsMetaType.NVDS_DISPLAY_META, 'NVDS_CLASSIFIER_META':
    # NvDsMetaType.NVDS_CLASSIFIER_META, 'NVDS_LABEL_INFO_META':
    # NvDsMetaType.NVDS_LABEL_INFO_META, 'NVDS_USER_META':
    # NvDsMetaType.NVDS_USER_META, 'NVDS_PAYLOAD_META':
    # NvDsMetaType.NVDS_PAYLOAD_META, 'NVDS_EVENT_MSG_META':
    # NvDsMetaType.NVDS_EVENT_MSG_META, 'NVDS_OPTICAL_FLOW_META':
    # NvDsMetaType.NVDS_OPTICAL_FLOW_META, 'NVDS_LATENCY_MEASUREMENT_META':
    # NvDsMetaType.NVDS_LATENCY_MEASUREMENT_META, 'NVDSINFER_TENSOR_OUTPUT_META':
    # NvDsMetaType.NVDSINFER_TENSOR_OUTPUT_META, 'NVDSINFER_SEGMENTATION_META':
    # NvDsMetaType.NVDSINFER_SEGMENTATION_META, 'NVDS_CROP_IMAGE_META':
    # NvDsMetaType.NVDS_CROP_IMAGE_META, 'NVDS_TRACKER_PAST_FRAME_META':
    # NvDsMetaType.NVDS_TRACKER_PAST_FRAME_META, 'NVDS_AUDIO_BATCH_META':
    # NvDsMetaType.NVDS_AUDIO_BATCH_META, 'NVDS_AUDIO_FRAME_META':
    # NvDsMetaType.NVDS_AUDIO_FRAME_META, 'NVDS_RESERVED_META':
    # NvDsMetaType.NVDS_RESERVED_META, 'NVDS_GST_CUSTOM_META':
    # NvDsMetaType.NVDS_GST_CUSTOM_META, 'NVDS_START_USER_META':
    # NvDsMetaType.NVDS_START_USER_META, 'NVDS_FORCE32_META':
    # NvDsMetaType.NVDS_FORCE32_META}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str."""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvDsMetaType, arg0: int) -> None."""

    def __index__(self) -> int: ...
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...

class NvDsObjectMeta:
    """Holds information of object metadata in the frame.

    :ivar base_meta: :class:`NvDsBaseMeta`, base_meta
    :ivar parent: the parent :class:`NvDsObjectMeta` object. Set to None if parent is
    not present
    :ivar unique_component_id: *int*, unique component id that attaches
    NvDsObjectMeta metadata
    :ivar class_id: *int*, Index of the object class infered by the primary
    detector/classifier
    :ivar object_id: *int*, Unique ID for tracking the object. @ref
    UNTRACKED_OBJECT_ID indicates the object has not been tracked
    :ivar confidence: *float*, Holds a confidence value for the object, set by the
    inference component.
        Confidence will be set to -0.1, if "Group Rectangles" mode of clustering is
        chosen since the algorithm does not preserve confidence values.
        Also, for objects found by tracker and not inference component, confidence
        will be set to -0.1
    :ivar detector_bbox_info: :class:`NvDsComp_BboxInfo`, Holds a structure
    containing bounding box parameters of the object when detected by detector
    :ivar tracker_bbox_info: :class:`NvDsComp_BboxInfo`, Holds a structure containing
    bounding box coordinates of the object when processed by tracker
    :ivar tracker_confidence: *float*, Holds a confidence value for the object set by
    nvdcf_tracker. tracker_confidence will be set to -0.1 for KLT and IOU tracker
    :ivar rect_params: :class:`NvOSD_RectParams`, Structure containing the positional
    parameters of the object in the frame.
        e.g. If the tracker component is after the detector component in the
        pipeline, then positional parameters are from tracker component.
        Can also be used to overlay borders / semi-transparent boxes on top of
        objects. See :class:`NvOSD_RectParams`
    :ivar mask_params: :class:`NvOSD_MaskParams`, Holds mask parameters for the
    object. This mask is overlaid on object See :class:`NvOSD_MaskParams`
    :ivar text_params: :class:`NvOSD_TextParams`, Text describing the object can be
    overlayed using this structure. See :class:`NvOSD_TextParams`
    :ivar obj_label: An array to store the string describing the class of the
    detected object
    :ivar classifier_meta_list: list of objects of type :class:`NvDsClassifierMeta`
    :ivar obj_user_meta_list: list of objects of type :class:`NvDsUserMeta`
    :ivar misc_obj_info: *list of int*, For additional user specific batch info
    :ivar reserved: *int*, Reserved for internal use.

    Example usage:
    ::

        #Initialize dict to keep count of objects of each type
        obj_counter = {
                PGIE_CLASS_ID_VEHICLE:0,
                PGIE_CLASS_ID_PERSON:0,
                PGIE_CLASS_ID_BICYCLE:0,
                PGIE_CLASS_ID_ROADSIGN:0
            }

        l_obj=frame_meta.obj_meta_list #Retrieve list of NvDsObjectMeta objects in
        frame from an NvDsFrameMeta object. See NvDsFrameMeta documentation for more
        details.
        while l_obj is not None:
            try:
                # Casting l_obj.data to pyds.NvDsObjectMeta
                obj_meta=pyds.NvDsObjectMeta.cast(l_obj.data)
                except StopIteration:
                    break
                obj_counter[obj_meta.class_id] += 1 #Retrieve class_id from
                NvDsObjectMeta (i.e. PGIE_CLASS_ID_VEHICLE, PGIE_CLASS_ID_PERSON,
                etc.) to update count
                obj_meta.rect_params.border_color.set(0.0, 0.0, 1.0, 0.0) #Set border
                color of NvDsObjectMeta object's rect_params
                try:
                    l_obj=l_obj.next
                except StopIteration:
                    break
    """

    base_meta: NvDsBaseMeta
    class_id: int
    classifier_meta_list: GList[NvDsClassifierMeta]
    confidence: float
    detector_bbox_info: NvDsComp_BboxInfo
    mask_params: NvOSD_MaskParams
    obj_label: str
    obj_user_meta_list: GList[NvDsUserMeta]
    object_id: int
    parent: NvDsObjectMeta
    rect_params: NvOSD_RectParams
    text_params: NvOSD_TextParams
    tracker_bbox_info: NvDsComp_BboxInfo
    tracker_confidence: float
    unique_component_id: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsObjectMeta]) -> NvDsObjectMeta:
        """Cast given object/data to :class:`NvDsObjectMeta`,
        call pyds.NvDsObjectMeta.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsObjectMeta:
        """Cast given object/data to :class:`NvDsObjectMeta`,
        call pyds.NvDsObjectMeta.cast(data).
        """

    @property
    def misc_obj_info(self) -> numpy.ndarray: ...
    @misc_obj_info.setter
    def misc_obj_info(self) -> None: ...
    @property
    def reserved(self) -> numpy.ndarray: ...
    @reserved.setter
    def reserved(self) -> None: ...

class NvDsObjectSignature:
    """Holds object signature.

    :ivar signature: *list of float*, Holds signature values.
    :ivar size: *int*, Holds the number of signature values in signature.
    """

    signature: float
    size: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsObjectSignature]) -> NvDsObjectSignature:
        """Cast given object/data to :class:`NvDsObjectSignature`,
        call pyds.NvDsObjectSignature.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsObjectSignature:
        """Cast given object/data to :class:`NvDsObjectSignature`,
        call pyds.NvDsObjectSignature.cast(data).
        """

class NvDsObjectType:
    """*Enumerator*. Object type flags.

    Members:

      NVDS_OBJECT_TYPE_VEHICLE : NVDS_OBJECT_TYPE_VEHICLE

      NVDS_OBJECT_TYPE_PERSON : NVDS_OBJECT_TYPE_PERSON

      NVDS_OBJECT_TYPE_FACE : NVDS_OBJECT_TYPE_FACE

      NVDS_OBJECT_TYPE_BAG : NVDS_OBJECT_TYPE_BAG

      NVDS_OBJECT_TYPE_BICYCLE : NVDS_OBJECT_TYPE_BICYCLE

      NVDS_OBJECT_TYPE_ROADSIGN : NVDS_OBJECT_TYPE_ROADSIGN

      NVDS_OBJECT_TYPE_VEHICLE_EXT : NVDS_OBJECT_TYPE_VEHICLE_EXT

      NVDS_OBJECT_TYPE_PERSON_EXT : NVDS_OBJECT_TYPE_PERSON_EXT

      NVDS_OBJECT_TYPE_FACE_EXT : NVDS_OBJECT_TYPE_FACE_EXT

      NVDS_OBJECT_TYPE_RESERVED : Reserved for future use. Use value greater than
    this for custom objects.

      NVDS_OBJECT_TYPE_CUSTOM : To support custom object.

      NVDS_OBJECT_TYPE_UNKNOWN : "object" key will be missing in the schema

      NVDS_OBEJCT_TYPE_FORCE32 : NVDS_OBEJCT_TYPE_FORCE32
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
    ]  # value = {'NVDS_OBJECT_TYPE_VEHICLE':
    # NvDsObjectType.NVDS_OBJECT_TYPE_VEHICLE, 'NVDS_OBJECT_TYPE_PERSON':
    # NvDsObjectType.NVDS_OBJECT_TYPE_PERSON, 'NVDS_OBJECT_TYPE_FACE':
    # NvDsObjectType.NVDS_OBJECT_TYPE_FACE, 'NVDS_OBJECT_TYPE_BAG':
    # NvDsObjectType.NVDS_OBJECT_TYPE_BAG, 'NVDS_OBJECT_TYPE_BICYCLE':
    # NvDsObjectType.NVDS_OBJECT_TYPE_BICYCLE, 'NVDS_OBJECT_TYPE_ROADSIGN':
    # NvDsObjectType.NVDS_OBJECT_TYPE_ROADSIGN, 'NVDS_OBJECT_TYPE_VEHICLE_EXT':
    # NvDsObjectType.NVDS_OBJECT_TYPE_VEHICLE_EXT, 'NVDS_OBJECT_TYPE_PERSON_EXT':
    # NvDsObjectType.NVDS_OBJECT_TYPE_PERSON_EXT, 'NVDS_OBJECT_TYPE_FACE_EXT':
    # NvDsObjectType.NVDS_OBJECT_TYPE_FACE_EXT, 'NVDS_OBJECT_TYPE_RESERVED':
    # NvDsObjectType.NVDS_OBJECT_TYPE_RESERVED, 'NVDS_OBJECT_TYPE_CUSTOM':
    # NvDsObjectType.NVDS_OBJECT_TYPE_CUSTOM, 'NVDS_OBJECT_TYPE_UNKNOWN':
    # NvDsObjectType.NVDS_OBJECT_TYPE_UNKNOWN, 'NVDS_OBEJCT_TYPE_FORCE32':
    # NvDsObjectType.NVDS_OBEJCT_TYPE_FORCE32}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str."""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvDsObjectType, arg0: int) -> None."""

    def __index__(self) -> int: ...
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...

class NvDsOpticalFlowMeta:
    """Holds optical flow metadata about a frame.

    :ivar rows: *int*, Number of rows present in the frame for given block size
        e.g. if block size is 4 and frame height is 720, then
        number of rows = (720 / 4) = 180
    :ivar cols: *int*, Number of columns present in the frame for given block size
        e.g. if block size is 4 and frame width is 1280, then
        number of columns = (1280 / 4) = 320
    :ivar mv_size: *int*, Size of motion vector. Refer :class:`NvOFFlowVector`.
    :ivar frame_num: *int*, Current frame number of the source.
    :ivar data: Holds the motion vector.
    :ivar priv: Reserved field, for internal purpose only.
    :ivar reserved: Reserved field, for internal purpose only.

    Example usage:
    ::

        def visualize_optical_flowvectors(flow):
            \"\"\"
            Converts the flow u, v vectors into visualization by mapping them into
            grey color space
            :param flow: flow vectors
            :return: bgr image
            \"\"\"
            shape_visual = (flow.shape[0], flow.shape[1], 3)
            mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
            hsv = np.full(shape_visual, 255, dtype=np.uint8)
            hsv[..., 1] = 255
            hsv[..., 0] = ang * 180 / np.pi / 2
            hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
            bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
            bgr = 255 - bgr
            return bgr

        ...

        l_user = frame_meta.frame_user_meta_list #Retrieve glist containing
        NvDsUserMeta objects from given NvDsFrameMeta object
        while l_user is not None:
            try:
                # Casting l_user.data to pyds.NvDsUserMeta
                of_user_meta = pyds.NvDsUserMeta.cast(l_user.data)
                except StopIteration:
                    break
                try:
                    # Casting of_user_meta.user_meta_data to pyds.NvDsOpticalFlowMeta
                    of_meta = pyds.NvDsOpticalFlowMeta.cast(of_user_meta.user_meta_data)
                    # Get Flow vectors as np array
                    flow_vectors = pyds.get_optical_flow_vectors(of_meta)
                    # Reshape the obtained flow vectors into proper shape
                    flow_vectors = flow_vectors.reshape(of_meta.rows, of_meta.cols, 2)
                    # map the flow vectors in HSV color space for visualization
                    flow_visual = visualize_optical_flowvectors(flow_vectors)
                    got_visual = True
                except StopIteration:
                    break
                try:
                    l_user = l_user.next
                except StopIteration:
                    break
    """

    cols: int
    data: typing.Any
    frame_num: int
    mv_size: int
    priv: typing.Any
    reserved: typing.Any
    rows: int

    def cast(self: capsule[NvDsOpticalFlowMeta]) -> NvDsOpticalFlowMeta:
        """Casts to :class:`NvDsOpticalFlowMeta`, call pyds.NvDsOpticalFlowMeta(
        data).
        """

class NvDsPastFrameObj:
    """NvDsPastFrameObj.

    :ivar frameNum: *int*, frameNum
    :ivar tBbox: :class:`NvOSD_RectParams`, tBbox
    :ivar confidence: *float*, confidence
    :ivar age: *int*, age

    Example usage:
    ::

        l_user=batch_meta.batch_user_meta_list #Retrieve glist of NvDsUserMeta
        objects from given NvDsBatchMeta object
        while l_user is not None:
            try:
                # Note that l_user.data needs a cast to pyds.NvDsUserMeta
                # The casting is done by pyds.NvDsUserMeta.cast()
                # The casting also keeps ownership of the underlying memory
                # in the C code, so the Python garbage collector will leave
                # it alone
                user_meta=pyds.NvDsUserMeta.cast(l_user.data)
            except StopIteration:
                break
            if(user_meta and user_meta.base_meta.meta_type==pyds.NvDsMetaType
            .NVDS_TRACKER_PAST_FRAME_META): #Make sure metatype is correct
                try:
                    # Note that user_meta.user_meta_data needs a cast to
                    pyds.NvDsPastFrameObjBatch
                    # The casting is done by pyds.NvDsPastFrameObjBatch.cast()
                    # The casting also keeps ownership of the underlying memory
                    # in the C code, so the Python garbage collector will leave
                    # it alone
                    pPastFrameObjBatch = pyds.NvDsPastFrameObjBatch.cast(
                    user_meta.user_meta_data) #See NvDsPastFrameObjBatch for details
                except StopIteration:
                    break
                for trackobj in pyds.NvDsPastFrameObjBatch.list(pPastFrameObjBatch):
                #Iterate through list of NvDsPastFrameObjStream objects
                    #Access NvDsPastFrameObjStream attributes
                    print("streamId=",trackobj.streamID)
                    print("surfaceStreamID=",trackobj.surfaceStreamID)
                    for pastframeobj in pyds.NvDsPastFrameObjStream.list(trackobj):
                    #Iterate through list of NvDsFrameObjList objects
                    #Access NvDsPastFrameObjList attributes
                    print("numobj=",pastframeobj.numObj)
                    print("uniqueId=",pastframeobj.uniqueId)
                    print("classId=",pastframeobj.classId)
                    print("objLabel=",pastframeobj.objLabel)
                    for objlist in pyds.NvDsPastFrameObjList.list(pastframeobj):
                    #Iterate through list of NvDsFrameObj objects
                        #Access NvDsPastFrameObj attributes
                        print('frameNum:', objlist.frameNum)
                        print('tBbox.left:', objlist.tBbox.left)
                        print('tBbox.width:', objlist.tBbox.width)
                        print('tBbox.top:', objlist.tBbox.top)
                        print('tBbox.right:', objlist.tBbox.height)
                        print('confidence:', objlist.confidence)
                        print('age:', objlist.age)
            try:
                l_user=l_user.next
            except StopIteration:
                break
    """

    age: int
    confidence: float
    frameNum: int
    tBbox: NvOSD_RectParams

    def __init__(self) -> None: ...
    def cast(self: capsule[NvDsPastFrameObj]) -> NvDsPastFrameObj:
        """Cast given object/data to :class:`NvDsPastFrameObj`,
        call pyds.NvDsPastFrameObj.cast(data).
        """

class NvDsPastFrameObjBatch:
    """Batch of lists of buffered objects. See :class:`NvDsPastFrameObj` for example
    usage.

    :ivar numAllocated: *int*, Number of blocks allocated for the list.
    :ivar numFilled: *int*, Number of filled blocks in the list.

    """

    numAllocated: int
    numFilled: int

    def __init__(self) -> None: ...
    def cast(self: capsule[NvDsPastFrameObjBatch]) -> NvDsPastFrameObjBatch:
        """Cast given object/data to :class:`NvDsPastFrameObjBatch`,
        call pyds.NvDsPastFrameObjBatch.cast(data).
        """

    def list(self) -> typing.Iterator:
        """Retrieve :class:`NvDsPastFrameObjBatch` object as list of
        :class:`NvDsPastFrameObjStream`. Contains stream lists.
        """

class NvDsPastFrameObjList:
    """One object in several past frames. See :class:`NvDsPastFrameObj` for example
    usage.

    :ivar numObj: *int*, Number of frames this object appreared in the past.
    :ivar uniqueId: *int*, Object tracking id.
    :ivar classID: *int*, Object class id.
    :ivar objLabel: An array of the string describing the object class.
    """

    classId: int
    numObj: int
    objLabel: str
    uniqueId: int

    def __init__(self) -> None: ...
    def cast(self: capsule[NvDsPastFrameObjList]) -> NvDsPastFrameObjList:
        """Cast given object/data to :class:`NvDsPastFrameObjList`,
        call pyds.NvDsPastFrameObjList.cast(data).
        """

    def list(self) -> typing.Iterator:
        """Retrieve :class:`NvDsPastFrameObjList` object as list of
        :class:`NvDsPastFrameObj`. Contains past frame info of this object.
        """

class NvDsPastFrameObjStream:
    """List of objects in each stream. See :class:`NvDsPastFrameObj` for example usage.

    :ivar streamID: *int*, Stream id the same as frame_meta->pad_index.
    :ivar surfaceStreamID: *int*, Stream id used inside tracker plugin.
    :ivar numAllocated: *int*, Maximum number of objects allocated.
    :ivar numFilled: *int*, Number of objects in this frame.
    """

    numAllocated: int
    numFilled: int
    streamID: int
    surfaceStreamID: int

    def __init__(self) -> None: ...
    def cast(self: capsule[NvDsPastFrameObjStream]) -> NvDsPastFrameObjStream:
        """Cast given object/data to :class:`NvDsPastFrameObjStream`,
        call pyds.NvDsPastFrameObjStream.cast(data).
        """

    def list(self) -> typing.Iterator:
        """Retrieve :class:`NvDsPastFrameObjStream` object as list of
        :class:`NvDsPastFrameObjList`. Contains objects inside this stream.
        """

class NvDsPayload:
    """Holds payload meta data.

    :ivar payload: Payload object.
    :ivar payloadSize: *int*, Size of payload.
    :ivar componentId: *int*, ID of component who attached the payload (Optional).
    """

    componentId: int
    payload: typing.Any
    payloadSize: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsPayload]) -> NvDsPayload:
        """Cast given object/data to :class:`NvDsPayload`,
        call pyds.NvDsPayload.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsPayload:
        """Cast given object/data to :class:`NvDsPayload`,
        call pyds.NvDsPayload.cast(data).
        """

class NvDsPayloadType:
    """*Enumerator*. Payload type flags.

    Members:

      NVDS_PAYLOAD_DEEPSTREAM : NVDS_PAYLOAD_DEEPSTREAM

      NVDS_PAYLOAD_DEEPSTREAM_MINIMAL : NVDS_PAYLOAD_DEEPSTREAM_MINIMAL

      NVDS_PAYLOAD_RESERVED : Reserved for future use. Use value greater than this
      for custom payloads.

      NVDS_PAYLOAD_CUSTOM : To support custom payload. User need to implement
      nvds_msg2p_* interface

      NVDS_PAYLOAD_FORCE32 : NVDS_PAYLOAD_FORCE32
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
    # NvDsPayloadType.NVDS_PAYLOAD_DEEPSTREAM_MINIMAL, 'NVDS_PAYLOAD_RESERVED':
    # NvDsPayloadType.NVDS_PAYLOAD_RESERVED, 'NVDS_PAYLOAD_CUSTOM':
    # NvDsPayloadType.NVDS_PAYLOAD_CUSTOM, 'NVDS_PAYLOAD_FORCE32':
    # NvDsPayloadType.NVDS_PAYLOAD_FORCE32}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str."""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvDsPayloadType, arg0: int) -> None."""

    def __index__(self) -> int: ...
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...

class NvDsPersonObject:
    """Holds a person object's parameters.

    :ivar gender: *str*, Person's gender.
    :ivar hair: *str*, Person's hair color.
    :ivar cap: *str*, Type of cap the person is wearing, if any.
    :ivar apparel: *str*, Description of the person's apparel.
    :ivar age: *int*, Person's age.

    Example usage:
    ::

        data = pyds.alloc_nvds_person_object() #Allocate NvDsPersonObject
        obj = pyds.NvDsPersonObject.cast(data)
        #Set attributes
        obj.age = 45
        obj.cap = "none"
        obj.hair = "black"
        obj.gender = "male"
        obj.apparel= "formal"
    """

    age: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsPersonObject]) -> NvDsPersonObject:
        """Casts to :class:`NvDsPersonObject` object, call pyds.NvDsPersonObject(
        data).
        """

    @typing.overload
    def cast(self: int) -> NvDsPersonObject:
        """Casts to :class:`NvDsPersonObject` object, call pyds.NvDsPersonObject(
        data).
        """

    @property
    def apparel(self) -> int: ...
    @apparel.setter
    def apparel(self, arg1: str) -> None: ...
    @property
    def cap(self) -> int: ...
    @cap.setter
    def cap(self, arg1: str) -> None: ...
    @property
    def gender(self) -> int: ...
    @gender.setter
    def gender(self, arg1: str) -> None: ...
    @property
    def hair(self) -> int: ...
    @hair.setter
    def hair(self, arg1: str) -> None: ...

class NvDsPersonObjectExt:
    """Holds a vehicle object's parameters.

    :ivar gender: *str*, Person's gender.
    :ivar hair: *str*, Person's hair color.
    :ivar cap: *str*, Type of cap the person is wearing, if any.
    :ivar apparel: *str*, Description of the person's apparel.
    :ivar age: *int*, Person's age.
    :ivar mask: *Glist* of polygons for person mask.
    """

    age: int
    apparel: str
    cap: str
    gender: str
    hair: str
    mask: GList[typing.Any]

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsPersonObjectExt]) -> NvDsPersonObjectExt:
        """Cast given object/data to :class:`NvDsPersonObjectExt`,
        call pyds.NvDsPersonObjectExt.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsPersonObjectExt:
        """Cast given object/data to :class:`NvDsPersonObjectExt`,
        call pyds.NvDsPersonObjectExt.cast(data).
        """

class NvDsRect:
    """Holds a rectangle's position and size.

    :ivar top: *float*, Holds the position of rectangle's top in pixels.
    :ivar left: *float*, Holds the position of rectangle's left side in pixels.
    :ivar width: *float*, Holds the rectangle's width in pixels.
    :ivar height: *float*, Holds the rectangle's height in pixels.
    """

    height: float
    left: float
    top: float
    width: float

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsRect]) -> NvDsRect:
        """Cast given object/data to :class:`NvDsRect`, call pyds.NvDsRect.cast(
        data).
        """

    @typing.overload
    def cast(self: int) -> NvDsRect:
        """Cast given object/data to :class:`NvDsRect`, call pyds.NvDsRect.cast(
        data).
        """

class NvDsUserMeta:
    """Holds information of user metadata that user can specify.

    :ivar base_meta: :class:`NvDsBaseMeta`, base_meta
    :ivar user_meta_data: User data object to be attached. Refer to
    deepstream-user-metadata-test example for usage.

    Example usage, where user metadata is of type NVDS_TRACKER_PAST_FRAME_META:
    ::

        l_user=batch_meta.batch_user_meta_list #Retrieve glist containing
        NvDsUserMeta objects from given NvDsBatchMeta object
        while l_user is not None:
            try:
                # Note that l_user.data needs a cast to pyds.NvDsUserMeta
                # The casting is done by pyds.NvDsUserMeta.cast()
                # The casting also keeps ownership of the underlying memory
                # in the C code, so the Python garbage collector will leave
                # it alone
                user_meta=pyds.NvDsUserMeta.cast(l_user.data)
            except StopIteration:
                break
            if(user_meta and user_meta.base_meta.meta_type==pyds.NvDsMetaType
            .NVDS_TRACKER_PAST_FRAME_META): #Check data type of user_meta
                try:
                    # Note that user_meta.user_meta_data needs a cast to
                    pyds.NvDsPastFrameObjBatch
                    # The casting is done by pyds.NvDsPastFrameObjBatch.cast()
                    # The casting also keeps ownership of the underlying memory
                    # in the C code, so the Python garbage collector will leave
                    # it alone
                    pPastFrameObjBatch = pyds.NvDsPastFrameObjBatch.cast(
                    user_meta.user_meta_data)
                except StopIteration:
                    break
                for trackobj in pyds.NvDsPastFrameObjBatch.list(pPastFrameObjBatch):
                    ... #Examine past frame information, see NvDsTrackerMeta docs for
                    details.
                try:
                    l_user=l_user.next
                except StopIteration:
                    break
    """

    base_meta: NvDsBaseMeta
    user_meta_data: typing.Any

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsUserMeta]) -> NvDsUserMeta:
        """Cast given object/data to :class:`NvDsUserMeta`,
        call pyds.NvDsUserMeta.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsUserMeta:
        """Cast given object/data to :class:`NvDsUserMeta`,
        call pyds.NvDsUserMeta.cast(data).
        """

class NvDsVehicleObject:
    """Holds vehicle object parameters.

    :ivar type: *str*, Type of the vehicle.
    :ivar make: *str*, Make of the vehicle.
    :ivar model: *str*, Model of the vehicle.
    :ivar color: *str*, Color of the vehicle.
    :ivar region: *str*, Region of the vehicle.
    :ivar license: *str*, License number of the vehicle.

    Example usage:
    ::

        data = pyds.alloc_nvds_vehicle_object() #Allocate NvDsVehicleObject
        obj = pyds.NvDsVehicleObject.cast(data);
        #Set attributes
        obj.type ="sedan"
        obj.color="blue"
        obj.make ="Bugatti"
        obj.model = "M"
        obj.license ="XX1234"
        obj.region ="CA"
    """

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsVehicleObject]) -> NvDsVehicleObject:
        """Casts to :class:`NvDsVehicleObject` object, call pyds.NvDsVehicleObject(
        data).
        """

    @typing.overload
    def cast(self: int) -> NvDsVehicleObject:
        """Casts to :class:`NvDsVehicleObject` object, call pyds.NvDsVehicleObject(
        data).
        """

    @property
    def color(self) -> int: ...
    @color.setter
    def color(self, arg1: str) -> None: ...
    @property
    def license(self) -> int: ...
    @license.setter
    def license(self, arg1: str) -> None: ...
    @property
    def make(self) -> int: ...
    @make.setter
    def make(self, arg1: str) -> None: ...
    @property
    def model(self) -> int: ...
    @model.setter
    def model(self, arg1: str) -> None: ...
    @property
    def region(self) -> int: ...
    @region.setter
    def region(self, arg1: str) -> None: ...
    @property
    def type(self) -> int: ...
    @type.setter
    def type(self, arg1: str) -> None: ...

class NvDsVehicleObjectExt:
    """Holds a vehicle object's parameters.

    :ivar type: *str*, Type of the vehicle.
    :ivar make: *str*, Make of the vehicle.
    :ivar model: *str*, Model of the vehicle.
    :ivar color: *str*, Color of the vehicle.
    :ivar region: *str*, Region of the vehicle.
    :ivar license: *str*, License number of the vehicle.
    :ivar mask: *Glist* of polygons for vehicle mask.
    """

    color: str
    license: str
    make: str
    mask: GList[typing.Any]
    model: str
    region: str
    type: str

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvDsVehicleObjectExt]) -> NvDsVehicleObjectExt:
        """Cast given object/data to :class:`NvDsVehicleObjectExt`,
        call pyds.NvDsVehicleObjectExt.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvDsVehicleObjectExt:
        """Cast given object/data to :class:`NvDsVehicleObjectExt`,
        call pyds.NvDsVehicleObjectExt.cast(data).
        """

class NvOFFlowVector:
    """Holds motion vector information about an element.

    :ivar flowx: *int*, x component of motion vector
    :ivar flowy: *int*, y component of motion vector
    """

    flowx: int
    flowy: int

    @typing.overload
    def cast(self: capsule[NvOFFlowVector]) -> NvOFFlowVector:
        """Casts to :class:`NvOFFlowVector`, call pyds.NvOFFlowVector(data)."""

    @typing.overload
    def cast(self: int) -> NvOFFlowVector:
        """Casts to :class:`NvOFFlowVector`, call pyds.NvOFFlowVector(data)."""

class NvOSD_ArrowParams:
    """Holds arrow parameters to be overlaid.

    :ivar x1: *int*, Holds start horizontal coordinate in pixels.
    :ivar y1: *int*, Holds start vertical coordinate in pixels.
    :ivar x2: *int*, Holds end horizontal coordinate in pixels.
    :ivar y2: *int*, Holds end vertical coordinate in pixels.
    :ivar arrow_width: *int*, Holds the arrow shaft width in pixels.
    :ivar arrow_color: :class:`NvOSD_ColorParams`, Holds the color parameters of the
    arrow box.
    :ivar arrow_head: :class:`NvOSD_Arrow_Head_Direction`, Holds the arrowhead position.
    :ivar reserved: *int*, reserved field for future usage. For internal purpose only.
    """

    arrow_color: NvOSD_ColorParams
    arrow_head: NvOSD_Arrow_Head_Direction
    arrow_width: int
    reserved: int
    x1: int
    x2: int
    y1: int
    y2: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvOSD_ArrowParams]) -> NvOSD_ArrowParams:
        """Cast given object/data to :class:`NvOSD_ArrowParams`,
        call pyds.NvOSD_ArrowParams.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvOSD_ArrowParams:
        """Cast given object/data to :class:`NvOSD_ArrowParams`,
        call pyds.NvOSD_ArrowParams.cast(data).
        """

class NvOSD_Arrow_Head_Direction:
    """*Enumerator*. Lists arrow head positions.

    Members:

      START_HEAD : Arrow head only at start = 0.

      END_HEAD : Arrow head only at end = 1.

      BOTH_HEAD : Arrow head at both sides = 2.
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
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str."""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvOSD_Arrow_Head_Direction, arg0: int) -> None."""

    def __index__(self) -> int: ...
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...

class NvOSD_CircleParams:
    """Holds the circle parameters to be overlayed.

       :ivar xc: *int*, Holds start horizontal coordinate in pixels.
       :ivar yc: *int*, Holds start vertical coordinate in pixels.
       :ivar radius: *int*, Holds radius of circle in pixels.
       :ivar circle_color: :class:`NvOSD_ColorParams`, Holds color params of the circle.
       :ivar has_bg_color: *int*, Holds boolean value indicating whethercircle has
    background color.
       :ivar bg_color: :class:`NvOSD_ColorParams`, Holds the circle's background color.
       :ivar reserved: *int*, Reserved field for future usage. For internal purpose
       only.
    """

    bg_color: NvOSD_ColorParams
    circle_color: NvOSD_ColorParams
    has_bg_color: int
    radius: int
    reserved: int
    xc: int
    yc: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvOSD_CircleParams]) -> NvOSD_CircleParams:
        """Cast given object/data to :class:`NvOSD_CircleParams`,
        call pyds.NvOSD_CircleParams.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvOSD_CircleParams:
        """Cast given object/data to :class:`NvOSD_CircleParams`,
        call pyds.NvOSD_CircleParams.cast(data).
        """

class NvOSD_ColorParams:
    """Holds the color parameters of the box or text to be overlayed. See
    :class:`NvOSD_TextParams` docs for example usage.

    :ivar red: *float*, Holds red component of color. Value must be in the range 0-1.
    :ivar green: *float*, Holds green component of color. Value must be in the range
    0-1.
    :ivar blue: *float*, Holds blue component of color. Value must be in the range 0-1.
    :ivar alpha: *float*, Holds alpha component of color. Value must be in the range
    0-1.
    """

    alpha: float
    blue: float
    green: float
    red: float

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvOSD_ColorParams]) -> NvOSD_ColorParams:
        """Cast given object/data to :class:`NvOSD_ColorParams`,
        call pyds.NvOSD_ColorParams.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvOSD_ColorParams:
        """Cast given object/data to :class:`NvOSD_ColorParams`,
        call pyds.NvOSD_ColorParams.cast(data).
        """

    def set(self, red: float, green: float, blue: float, alpha: float) -> None:
        """Sets the color values.

        :arg red: Value for red component (must be in range 0.-1.)
        :arg green: Value for green component (must be in range 0.-1.)
        :arg blue: Value for blue component (must be in range 0.-1.)
        :arg alpha: Value for alpha component (must be in range 0.-1.)
        """

class NvOSD_Color_info:
    """NvOSD_Color_info.

    :ivar id: id
    :ivar color: color
    """

    color: NvOSD_ColorParams
    id: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvOSD_Color_info]) -> NvOSD_Color_info:
        """Cast given object/data to :class:`NvOSD_Color_info`,
        call pyds.NvOSD_Color_info.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvOSD_Color_info:
        """Cast given object/data to :class:`NvOSD_Color_info`,
        call pyds.NvOSD_Color_info.cast(data).
        """

class NvOSD_FontParams:
    """Holds the font parameters of the text to be overlayed. See
    :class:`NvOSD_TextParams` docs for example usage.

    :ivar fontname: *str*, Holds the font name. The list of supported fonts can be
    obtained by running fc-list command
    :ivar fontsize: *int*, Holds size of the font.
    :ivar fontcolor: :class:`NvOSD_ColorParams`, Holds the font color.
    """

    font_color: NvOSD_ColorParams
    font_size: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvOSD_FontParams]) -> NvOSD_FontParams:
        """Cast given object/data to :class:`NvOSD_FontParams`,
        call pyds.NvOSD_FontParams.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvOSD_FontParams:
        """Cast given object/data to :class:`NvOSD_FontParams`,
        call pyds.NvOSD_FontParams.cast(data).
        """

    @property
    def font_name(self) -> int: ...
    @font_name.setter
    def font_name(self, arg1: str) -> None: ...

class NvOSD_FrameArrowParams:
    """Holds information about the arrows in a frame.

    :ivar buf_ptr: :class:`NvBufSurfaceParams`, Holds the buffer containing frame.
    :ivar mode: :class:`NvOSD_Mode`, Holds OSD Mode to be used for processing.
    :ivar num_arrows: *int*, Holds number of arrows.
    :ivar arrow_params_list: list of :class:`NvOSD_ArrowParams`, Holds the arrows'
    parameters.
    """

    arrow_params_list: NvOSD_ArrowParams
    buf_ptr: NvBufSurfaceParams
    mode: NvOSD_Mode
    num_arrows: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvOSD_FrameArrowParams]) -> NvOSD_FrameArrowParams:
        """Cast given object/data to :class:`NvOSD_FrameArrowParams`,
        call pyds.NvOSD_FrameArrowParams.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvOSD_FrameArrowParams:
        """Cast given object/data to :class:`NvOSD_FrameArrowParams`,
        call pyds.NvOSD_FrameArrowParams.cast(data).
        """

class NvOSD_FrameCircleParams:
    """Holds information about the circles in a frame.

    :ivar buf_ptr: :class:`NvBufSurfaceParams`, Holds the buffer containing frame.
    :ivar mode: :class:`NvOSD_Mode`, Holds OSD Mode to be used for processing.
    :ivar num_circles: *int*, Holds number of circles.
    :ivar circle_params_list: list of :class:`NvOSD_CircleParams`, Holds the circles'
    parameters.
    """

    buf_ptr: NvBufSurfaceParams
    circle_params_list: NvOSD_CircleParams
    mode: NvOSD_Mode
    num_circles: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvOSD_FrameCircleParams]) -> NvOSD_FrameCircleParams:
        """Cast given object/data to :class:`NvOSD_FrameCircleParams`,
        call pyds.NvOSD_FrameCircleParams.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvOSD_FrameCircleParams:
        """Cast given object/data to :class:`NvOSD_FrameCircleParams`,
        call pyds.NvOSD_FrameCircleParams.cast(data).
        """

class NvOSD_FrameLineParams:
    """Holds information about the lines in a frame.

    :ivar buf_ptr: :class:`NvBufSurfaceParams`, Holds the buffer containing frame.
    :ivar mode: :class:`NvOSD_Mode`, Holds OSD Mode to be used for processing.
    :ivar num_lines: *int*, Holds number of lines.
    :ivar line_params_list: list of :class:`NvOSD_LineParams`, Holds the lines'
    parameters.
    """

    buf_ptr: NvBufSurfaceParams
    line_params_list: NvOSD_LineParams
    mode: NvOSD_Mode
    num_lines: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvOSD_FrameLineParams]) -> NvOSD_FrameLineParams:
        """Cast given object/data to :class:`NvOSD_FrameLineParams`,
        call pyds.NvOSD_FrameLineParams.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvOSD_FrameLineParams:
        """Cast given object/data to :class:`NvOSD_FrameLineParams`,
        call pyds.NvOSD_FrameLineParams.cast(data).
        """

class NvOSD_FrameRectParams:
    """Holds information about the rectangles in a frame.

    :ivar buf_ptr: :class:`NvBufSurfaceParams`, Holds the buffer containing frame.
    :ivar mode: :class:`NvOSD_Mode`, Holds OSD Mode to be used for processing.
    :ivar num_rects: *int*, Holds number of rectangles.
    :ivar rect_params_list: list of :class:`NvOSD_RectParams`, Holds the rectangles'
    parameters.
    """

    buf_ptr: NvBufSurfaceParams
    mode: NvOSD_Mode
    num_rects: int
    rect_params_list: NvOSD_RectParams

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvOSD_FrameRectParams]) -> NvOSD_FrameRectParams:
        """Cast given object/data to :class:`NvOSD_FrameRectParams`,
        call pyds.NvOSD_FrameRectParams.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvOSD_FrameRectParams:
        """Cast given object/data to :class:`NvOSD_FrameRectParams`,
        call pyds.NvOSD_FrameRectParams.cast(data).
        """

class NvOSD_FrameTextParams:
    """Holds information about the text in a frame.

    :ivar buf_ptr: :class:`NvBufSurfaceParams`, Holds the buffer containing frame.
    :ivar mode: :class:`NvOSD_Mode`, Holds OSD Mode to be used for processing.
    :ivar num_strings: *int*, Holds number of strings.
    :ivar text_params_list: list of :class:`NvOSD_TextParams`, Holds the strings'
    text parameters.
    """

    buf_ptr: NvBufSurfaceParams
    mode: NvOSD_Mode
    num_strings: int
    text_params_list: NvOSD_TextParams

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvOSD_FrameTextParams]) -> NvOSD_FrameTextParams:
        """Cast given object/data to :class:`NvOSD_FrameTextParams`,
        call pyds.NvOSD_FrameTextParams.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvOSD_FrameTextParams:
        """Cast given object/data to :class:`NvOSD_FrameTextParams`,
        call pyds.NvOSD_FrameTextParams.cast(data).
        """

class NvOSD_LineParams:
    """Holds the box parameters of the line to be overlaid.

    :ivar x1: *int*, Holds left coordinate of the box in pixels.
    :ivar y1: *int*, Holds top coordinate of the box in pixels.
    :ivar x2: *int*, Holds width of the box in pixels.
    :ivar y2: *int*, Holds height of the box in pixels.
    :ivar line_width: *int*, Holds border_width of the box in pixels.
    :ivar line_color: :class:`NvOSD_ColorParams`, Holds color params of the border of
    the box.
    """

    line_color: NvOSD_ColorParams
    line_width: int
    x1: int
    x2: int
    y1: int
    y2: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvOSD_LineParams]) -> NvOSD_LineParams:
        """Cast given object/data to :class:`NvOSD_LineParams`,
        call pyds.NvOSD_LineParams.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvOSD_LineParams:
        """Cast given object/data to :class:`NvOSD_LineParams`,
        call pyds.NvOSD_LineParams.cast(data).
        """

class NvOSD_MaskParams:
    """Holds the mask parameters of the segment to be overlayed.

    :ivar data: *float**, Mask buffer.
    :ivar size: *int*, Size of the mask buffer in bytes.
    :ivar threshold: *int*, Threshold for binarization.
    :ivar height: *int*, Mask height.
    :ivar width: *int*, Mask width.
    """

    data: float
    height: int
    size: int
    threshold: float
    width: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvOSD_MaskParams]) -> NvOSD_MaskParams:
        """Cast given object/data to :class:`NvOSD_MaskParams`,
        call pyds.NvOSD_MaskParams.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvOSD_MaskParams:
        """Cast given object/data to :class:`NvOSD_MaskParams`,
        call pyds.NvOSD_MaskParams.cast(data).
        """

    def get_mask_array(self) -> numpy.ndarray:
        """Retrieve mask data as numpy array."""

class NvOSD_Mode:
    """*Enumerator*. List modes used to overlay boxes and text.

    Members:

      MODE_CPU : Selects CPU for OSD processing. Works with RGBA data only.

      MODE_GPU : Selects GPU for OSD processing. Yet to be implemented.

      MODE_NONE : Invalid mode. Instead GPU mode will be used.
    """

    MODE_CPU: typing.ClassVar[NvOSD_Mode]  # value = NvOSD_Mode.MODE_CPU
    MODE_GPU: typing.ClassVar[NvOSD_Mode]  # value = NvOSD_Mode.MODE_GPU
    MODE_NONE: typing.ClassVar[NvOSD_Mode]  # value = NvOSD_Mode.MODE_NONE
    __members__: typing.ClassVar[
        dict[str, NvOSD_Mode]
    ]  # value = {'MODE_CPU': NvOSD_Mode.MODE_CPU, 'MODE_GPU': NvOSD_Mode.MODE_GPU,
    # 'MODE_NONE': NvOSD_Mode.MODE_NONE}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str."""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.NvOSD_Mode, arg0: int) -> None."""

    def __index__(self) -> int: ...
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...

class NvOSD_RectParams:
    """Holds the box parameters of the box to be overlaid.

    :ivar left: *float*, Holds left coordinate of the box in pixels.
    :ivar top: *float*, Holds top coordinate of the box in pixels.
    :ivar width: *float*, Holds width of the box in pixels.
    :ivar height: *float*, Holds height of the box in pixels.
    :ivar border_width: *int*, Holds border_width of the box in pixels.
    :ivar border_color: :class:`NvOSD_ColorParams`, Holds color params of the border
    of the box.
    :ivar has_bg_color: *int*, Holds boolean value indicating whether box has
    background color.
    :ivar bg_color: :class:`NvOSD_ColorParams`, Holds background color of the box.
    :ivar has_color_info: *int*, color_info
    :ivar color_id: *int*, id of the color
    :ivar reserved: *int*, Reserved field for future usage. For internal purpose only.
    """

    bg_color: NvOSD_ColorParams
    border_color: NvOSD_ColorParams
    border_width: int
    color_id: int
    has_bg_color: int
    has_color_info: int
    height: float
    left: float
    reserved: int
    top: float
    width: float

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvOSD_RectParams]) -> NvOSD_RectParams:
        """Cast given object/data to :class:`NvOSD_RectParams`,
        call pyds.NvOSD_RectParams.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvOSD_RectParams:
        """Cast given object/data to :class:`NvOSD_RectParams`,
        call pyds.NvOSD_RectParams.cast(data).
        """

class NvOSD_TextParams:
    """Holds the parameters of the text to be overlaid.

    :ivar display_text: *str*, Holds the text to be overlaid.
    :ivar x_offset: *int*, Holds horizontal offset w.r.t top left pixel of the frame.
    :ivar y_offset: *int*, Holds vertical offset w.r.t top left pixel of the frame.
    :ivar font_params: :class:`NvOSD_FontParams`, Holds the font parameters of the
    text to be overlaid.
    :ivar set_bg_clr: *int*, Boolean to indicate text has background color.
    :ivar text_bg_clr: :class:`NvOSD_ColorParams`, Holds the text's background color,
    if specified.

    Example usage:
    ::

        display_meta=pyds.nvds_acquire_display_meta_from_pool(batch_meta) #Retrieve
        NvDsDisplayMeta object from given NvDsBatchMeta object. See NvDsMeta docs for
        more details.
        display_meta.num_labels = 1
        py_nvosd_text_params = display_meta.text_params[0] #Retrieve NvOSD_TextParams
        object from list in display meta.
        # Setting display text to be shown on screen
        # Note that the pyds module allocates a buffer for the string, and the
        # memory will not be claimed by the garbage collector.
        # Reading the display_text field here will return the C address of the
        # allocated string. Use pyds.get_string() to get the string content.
        py_nvosd_text_params.display_text = "Frame Number={} Number of Objects={}
        Vehicle_count={} Person_count={}".format(frame_number, num_rects,
        obj_counter[PGIE_CLASS_ID_VEHICLE], obj_counter[PGIE_CLASS_ID_PERSON])

        # Now set the offsets where the string should appear
        py_nvosd_text_params.x_offset = 10
        py_nvosd_text_params.y_offset = 12

        # Font , font-color and font-size
        py_nvosd_text_params.font_params.font_name = "Serif" #Set attributes of our
        NvOSD_TextParams object's NvOSD_FontParams member
        py_nvosd_text_params.font_params.font_size = 10
        # set(red, green, blue, alpha); set to White
        py_nvosd_text_params.font_params.font_color.set(1.0, 1.0, 1.0, 1.0) #See
        NvOSD_ColorParams for more details.

        # Text background color
        py_nvosd_text_params.set_bg_clr = 1 #Set boolean indicating that text has bg
        color to true.
        # set(red, green, blue, alpha); set to Black
        py_nvosd_text_params.text_bg_clr.set(0.0, 0.0, 0.0, 1.0)
        # Using pyds.get_string() to get display_text as string
        print(pyds.get_string(py_nvosd_text_params.display_text))
        pyds.nvds_add_display_meta_to_frame(frame_meta, display_meta) #Add display
        meta to frame after setting text params attributes.
    """

    font_params: NvOSD_FontParams
    set_bg_clr: int
    text_bg_clr: NvOSD_ColorParams
    x_offset: int
    y_offset: int

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[NvOSD_TextParams]) -> NvOSD_TextParams:
        """Cast given object/data to :class:`NvOSD_TextParams`,
        call pyds.NvOSD_TextParams.cast(data).
        """

    @typing.overload
    def cast(self: int) -> NvOSD_TextParams:
        """Cast given object/data to :class:`NvOSD_TextParams`,
        call pyds.NvOSD_TextParams.cast(data).
        """

    @property
    def display_text(self) -> int: ...
    @display_text.setter
    def display_text(self, arg1: str) -> None: ...

class ROI_STATUS_360D:
    """*Enumerator*. Defines DeepStream 360d metadata.

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
    ]  # value = {'ROI_ENTRY_360D': ROI_STATUS_360D.ROI_ENTRY_360D, 'ROI_EXIT_360D':
    # ROI_STATUS_360D.ROI_EXIT_360D, 'INSIDE_AISLE_360D':
    # ROI_STATUS_360D.INSIDE_AISLE_360D}
    @staticmethod
    def __eq__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __getstate__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __hash__(*args, **kwargs):
        """(self: object) -> int_."""

    @staticmethod
    def __ne__(*args, **kwargs):
        """(self: object, arg0: object) -> bool."""

    @staticmethod
    def __repr__(*args, **kwargs):
        """(self: handle) -> str."""

    @staticmethod
    def __setstate__(*args, **kwargs):
        """(self: pyds.ROI_STATUS_360D, arg0: int) -> None."""

    def __index__(self) -> int: ...
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...

class RectDim:
    """RectDim.

    :ivar left: *float*, left
    :ivar top: *float*, top
    :ivar width: *float*, width
    :ivar height: *float*, height
    :ivar class_id: *int*, class_id
    :ivar tracking_id: *int*, tracking_id
    :ivar gie_unique_id: *int*, gie_unique_id
    :ivar roi_status: *int*, roi_status
    :ivar text: text
    :ivar left: *float*, left
    """

    class_id: int
    gie_unique_id: int
    height: float
    left: float
    roi_status: int
    text: typing.Any
    top: float
    tracking_id: int
    width: float

    def __init__(self) -> None: ...
    @typing.overload
    def cast(self: capsule[RectDim]) -> RectDim:
        """Cast given object/data to :class:`RectDim`, call pyds.RectDim.cast(data)."""

    @typing.overload
    def cast(self: int) -> RectDim:
        """Cast given object/data to :class:`RectDim`, call pyds.RectDim.cast(data)."""

def NvBufSurfaceCopy(srcSurf: NvBufSurface, dstSurf: NvBufSurface) -> int:
    """Copy the memory content of source batched buffer(s) to memory of destination
    batched buffer(s).

    This function can be used to copy source buffer(s) of one memory type
    to destination buffer(s) of different memory type.
    e.g. CUDA Host to CUDA Device or malloced memory to CUDA device etc.

    Both source and destination :class:`NvBufSurface` must have same buffer and batch
    size.

    :arg srcSurf: pointer to source :class:`NvBufSurface` structure.
    :arg dstSurf: pointer to destination :class:`NvBufSurface`  structure.

    :returns: 0 for success, -1 for failure.
    """

def NvBufSurfaceCreate(
    surf: NvBufSurface, batchSize: int, params: NvBufSurfaceCreateParams
) -> int:
    """Allocate batch of buffers.

    Allocates memory for batchSize buffers and returns in surf object allocated
    :class:`NvBufSurface`.
    params object should have allocation parameters of single object. If size field in
    params is set, buffer of that size will be allocated and all other
    parameters (w, h, color format etc.) will be ignored.

    Use :py:func:`NvBufSurfaceDestroy` to free all the resources.

    :arg surf: pointer to allocated batched buffers.
    :arg batchSize: batch size of buffers.
    :arg params: pointer to :class:`NvBufSurfaceCreateParams` structure.

    :returns: 0 for success, -1 for failure.
    """

def NvBufSurfaceDestroy(surf: NvBufSurface) -> int:
    """Free the batched buffers previously allocated through NvBufSurfaceCreate.

    :arg surf: An object to :class:`NvBufSurface` to free.

    :returns: 0 for success, -1 for failure.
    """

def NvBufSurfaceFromFd(dmabuf: int, buffer: capsule[NvBufSurface]) -> int:
    """Get the :class:`NvBufSurface` from the dmabuf fd.

    :arg dmabuf_fd: dmabuf fd of the buffer.
    :arg buffer: pointer to :class:`NvBufSurface` .

    :returns: 0 for success, -1 for failure.
    """

def NvBufSurfaceMap(
    surf: NvBufSurface, index: int, plane: int, type: NvBufSurfaceMemMapFlags
) -> int:
    """Map HW batched buffers to HOST CPU address space.

    Valid for NVBUF_MEM_CUDA_UNIFIED type of memory for dGPU and
    NVBUF_MEM_SURFACE_ARRAY and NVBUF_MEM_HANDLE type of memory for Jetson.

    This function will fill addr array of :class:`NvBufSurfaceMappedAddr` field of
    :class:`NvBufSurfaceParams` with the CPU mapped memory pointers.

    The client must call :py:func:`NvBufSurfaceSyncForCpu` with the virtual address
    populated by this function before accessing the mapped memory in CPU.

    After memory mapping is complete, mapped memory modification must be coordinated
    between the CPU and hardware device as follows:
        - CPU: If the CPU modifies any mapped memory, the client must call
        :py:func:`NvBufSurfaceSyncForDevice` before any hardware device accesses the
        memory.
        - Hardware device: If the mapped memory is modified by any hardware device,
        the client must call :py:func:`NvBufSurfaceSyncForCpu` before CPU accesses
        the memory.

    Use :py:func:`NvBufSurfaceUnMap` to unmap buffer(s) and release any resource.

    :arg surf: pointer to :class:`NvBufSurface` structure.
    :arg index: index of buffer in the batch. -1 for all buffers in batch.
    :arg plane: index of plane in buffer. -1 for all planes in buffer.
    :arg type: flag for mapping type.

    :returns: 0 for success, -1 for failure.
    """

def NvBufSurfaceMapEglImage(surf: NvBufSurface, index: int) -> int:
    """Creates an EGLImage from memory of :class:`NvBufSurface` buffer(s).

    Only memory type NVBUF_MEM_SURFACE_ARRAY is supported.
    This function will set eglImage pointer of :class:`NvBufSurfaceMappedAddr` field
    of :class:`NvBufSurfaceParams` with EGLImageKHR.

    This function can be used in scenarios where CUDA operation on Jetson HW
    memory (NVBUF_MEM_SURFACE_ARRAY) is required. EGLImageKHR provided by this
    function can then be register with CUDA for further CUDA operations.

    :arg surf: pointer to NvBufSurface structure.
    :arg index: index of buffer in the batch. -1 for all buffers in batch.

    :returns: 0 for success, -1 for failure.
    """

def NvBufSurfaceMemSet(surf: NvBufSurface, index: int, plane: int, value: int) -> int:
    """Fill each byte of buffer(s) in :class:`NvBufSurface` with provided value.

    This function can also be used to reset the buffer(s) in the batch.

    :arg surf: pointer to :class:`NvBufSurface` structure.
    :arg index: index of buffer in the batch. -1 for all buffers in batch.
    :arg plane: index of plane in buffer. -1 for all planes in buffer.
    :arg value: value to be set.

    :returns: 0 for success, -1 for failure.
    """

def NvBufSurfaceSyncForCpu(surf: NvBufSurface, index: int, plane: int) -> int:
    """Syncs the HW memory cache for the CPU.

    Valid only for NVBUF_MEM_SURFACE_ARRAY and NVBUF_MEM_HANDLE memory types.

    :arg surf: pointer to :class:`NvBufSurface` structure.
    :arg index: index of buffer in the batch. -1 for all buffers in batch.
    :arg plane: index of plane in buffer. -1 for all planes in buffer.

    :returns: 0 for success, -1 for failure.
    """

def NvBufSurfaceSyncForDevice(surf: NvBufSurface, index: int, plane: int) -> int:
    """Syncs the HW memory cache for the device.

    Valid only for NVBUF_MEM_SURFACE_ARRAY and NVBUF_MEM_HANDLE memory types.

    :arg surf: pointer to :class:`NvBufSurface` structure.
    :arg index: index of buffer in the batch. -1 for all buffers in batch.
    :arg plane: index of plane in buffer. -1 for all planes in buffer.

    :returns: 0 for success, -1 for failure.
    """

def NvBufSurfaceUnMap(surf: NvBufSurface, index: int, plane: int) -> int:
    """Unmap the previously mapped buffer(s).

    :arg surf: pointer to :class:`NvBufSurface` structure.
    :arg index: index of buffer in the batch. -1 for all buffers in batch.
    :arg plane: index of plane in buffer. -1 for all planes in buffer.

    :returns: 0 for success, -1 for failure.
    """

def alloc_buffer(size: int) -> int:
    """Allocate buffer of given size.

    :arg size: Size of memory to be allocated

    :returns: C address of allocated buffer
    """

def alloc_char_buffer(arg0: int) -> int: ...
def alloc_custom_struct(arg0: NvDsUserMeta) -> CustomDataStruct:
    """Allocate an :class:`CustomDataStruct`.

    :returns: Allocated :class:`CustomDataStruct`
    """

def alloc_nvds_event() -> NvDsEvent:
    """Allocate an :class:`NvDsEvent`.

    :returns: Allocated :class:`NvDsEvent`
    """

def alloc_nvds_event_msg_meta() -> NvDsEventMsgMeta:
    """Allocate an :class:`NvDsEventMsgMeta`.

    :returns: Allocated :class:`NvDsEventMsgMeta`
    """

def alloc_nvds_face_object() -> NvDsFaceObject:
    """Allocate an :class:`NvDsFaceObject`.

    :returns: Allocated :class:`NvDsFaceObject`
    """

def alloc_nvds_payload() -> NvDsPayload:
    """Allocate an :class:`NvDsPayload`.

    :returns: Allocated :class:`NvDsPayload`
    """

def alloc_nvds_person_object() -> NvDsPersonObject:
    """Allocate an :class:`NvDsPersonObject`.

    :returns: Allocated :class:`NvDsPersonObject`
    """

def alloc_nvds_vehicle_object() -> NvDsVehicleObject:
    """Allocate an :class:`NvDsVehicleObject`.

    :returns: Allocated :class:`NvDsVehicleObject`
    """

def configure_source_for_ntp_sync(src_elem: int) -> None:
    """Configure the source to generate NTP sync values for RTSP sources.

    These values are used by the DeepStream GStreamer element NvStreamMux to
    calculate the NTP time of the frames at the source.

    This functionality is dependent on the RTSP sending the RTCP Sender Reports. source.

    This function only works for RTSP sources i.e. GStreamer elements "rtspsrc" or
    "uridecodebin" with an RTSP uri.

    :arg src_elem: GStreamer source element to be configured.
    """

def free_buffer(buffer: int) -> None:
    """Frees memory of given buffer.

    :arg buffer: C address of the buffer to be freed
    """

def free_gbuffer(buffer: typing.Any) -> None:
    """Frees memory of given gbuffer.

    :arg buffer: gpointer to the buffer to be freed
    """

def generate_ts_rfc3339(buffer: int, size: int) -> None:
    """Generate RFC3339 timestamp.

    :arg buffer: Buffer into which timestamp content is copied
    :arg size: Maximum timestamp length
    """

def get_detections(arg0: typing.Any, arg1: int) -> float: ...
def get_nvds_LayerInfo(arg0: typing.Any, arg1: int) -> NvDsInferLayerInfo: ...
def get_nvds_buf_surface(gst_buffer: int, batchID: int) -> numpy.ndarray:
    """This function returns the frame in NumPy format. Only RGBA format is
    supported. For x86_64, only unified memory is supported. For Jetson, the buffer
    is mapped to CPU memory. Changes to the frame image will be preserved and seen in
    downstream elements, with the following restrictions.
    1. No change to image color format or resolution
    2. No transpose operation on the array.

    For Jetson, a matching call to :py:func:`unmap_nvds_buf_surface` must be made.

    :arg gst_buffer: address of the Gstbuffer which contains `NvBufSurface`
    :arg batchID: batch_id of the frame to be processed. This indicates the frame's
    index within :class:`NvBufSurface`

    :returns: NumPy array containing the frame image buffer.
    """

def get_nvds_buf_surface_gpu(gst_buffer: int, batchID: int) -> None:
    """This function returns the dtype, shape of the array, strides, pointer to the
    GPU buffer, and size of the allocated memory for the buffer. Only x86 and RGBA
    format is supported. This information can be used to create a CuPy array (see
    deepstream-imagedata-multistream-cupy).
    Changes to the frame image will be preserved and seen in downstream elements,
    with the following restrictions.
    1. No change to image color format or resolution
    2. No transpose operation on the array.

    :arg gst_buffer: address of the Gstbuffer which contains `NvBufSurface`
    :arg batchID: batch_id of the frame to be processed. This indicates the frame's
    index within :class:`NvBufSurface`

    :returns: dtype, shape, strides, pointer to buffer, size of allocated memory of
    the GPU buffer
    """

def get_optical_flow_vectors(
    data: capsule[NvDsOpticalFlowMeta],
) -> NDArray[numpy.float32]:
    """:arg of_meta: An object of type :class:`NvDsOpticalFlowMeta`.

    :returns: Interleaved x, y directed optical flow vectors for a block of pixels in
    numpy format with shape (rows,cols,2), where rows and cols are the Optical flow
    outputs. These rows and cols are not equivalent to input resolution.
    """

def get_ptr(ptr: typing.Any) -> int:
    """Gets the C address of given object.

    :arg ptr: Object of which to retrieve C address "pointer"

    :returns: C address of given data
    """

def get_segmentation_masks(data: capsule[NvDsInferSegmentationMeta]) -> numpy.ndarray:
    """This function returns the inferred masks in Numpy format in the height X width
    shape, these height and width are obtained from the
    :class:`NvDsInferSegmentationMeta`.

    :arg data: An object of type :class:`NvDsInferSegmentationMeta`
    """

def get_string(ptr: int) -> str:
    """Cast given pointer to string.

    :arg ptr: C address of the string

    :returns: Reference to the string object
    """

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
    """Adds GstMeta of type :class:`NvDsMeta` to the GstBuffer and sets the
    `meta_data` member of :class:`NvDsMeta`.

    :arg buffer: GstBuffer to which the function adds metadata.
    :arg meta_data: The object to which the function sets the meta_data member of
    :class:`NvDsMeta`.
    :arg user_data: A user specific data object
    :arg copy_func: The NvDsMetaCopyFunc function to be called when NvDsMeta is to be
    copied. The function is called with meta_data and user_data as parameters.
    NvDsMeta is to be destroyed. The function is called with meta_data and user_data
    as parameters.

    :returns: An object to the attached :class:`NvDsMeta` object; or NONE in case
    failure
    """

def gst_buffer_get_nvds_batch_meta(buffer: int) -> NvDsBatchMeta:
    """Gets the :class:`NvDsBatchMeta` added to the GstBuffer.

    :arg buffer: GstBuffer from which to retrieve the :class:`NvDsBatchMeta`

    :returns: :class:`NvDsBatchMeta` object retrieved from the buffer

    For example:
    ``batch_meta = pyds.gst_buffer_get_nvds_batch_meta(hash(gst_buffer))``
    """

def gst_element_send_nvevent_new_stream_reset(arg0: int, arg1: int) -> int:
    """Sends a "custom reset" event on the given element for the specified source.
    This nvevent_new_stream_reset event is propogated downstream.

    This function, along with other reset events, can be used to reset the source
    in case RTSP reconnection is required.

    :arg gst_element: element for to which the generated event needs to be sent.
    :arg source_id: source id for which this event needs to be generated
    :returns: True for success.
    """

def memdup(ptr: int, size: int) -> int: ...
def nvds_acquire_classifier_meta_from_pool(
    batch_meta: NvDsBatchMeta,
) -> NvDsClassifierMeta:
    """Acquires :class:`NvDsClassifierMeta` from the classifier meta pool. User must
    acquire the classifier meta from the classifier meta pool to fill classifier
    metadata.

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` from which
    :class:`NvDsClassifierMeta` will be acquired

    :returns: Acquired :class:`NvDsClassifierMeta` object from classifier meta pool
    """

def nvds_acquire_display_meta_from_pool(batch_meta: NvDsBatchMeta) -> NvDsDisplayMeta:
    """Acquires NvDsDisplayMeta from the display meta pool. User must acquire the
    display meta from the display meta pool to fill display metadata.

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` from which
    :class:`NvDsDisplayMeta` will be acquired.

    :returns: Acquired :class:`NvDsDisplayMeta` object from display meta pool
    """

def nvds_acquire_frame_meta_from_pool(batch_meta: NvDsBatchMeta) -> NvDsFrameMeta:
    """Acquires :class:`NvDsFrameMeta` from frame_meta pool. User must acquire the
    frame_meta from frame_meta pool to fill frame metadata.

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` from which
    :class:`NvDsFrameMeta` will be acquired

    :returns: Acquired :class:`NvDsFrameMeta` object from frame meta pool
    """

def nvds_acquire_label_info_meta_from_pool(batch_meta: NvDsBatchMeta) -> NvDsLabelInfo:
    """Acquires :class:`NvDsLabelInfo` from the labelinfo meta pool of given
    :class:`NvDsBatchMeta`. User must acquire the labelinfo meta from the labelinfo
    meta pool to fill labelinfo metadata.

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` from which
    :class:`NvDsLabelInfo` will be acquired

    :returns: An object of type :class:`NvDsLabelInfo` object from label info meta pool
    """

def nvds_acquire_meta_lock(batch_meta: NvDsBatchMeta) -> None:
    """Acquire the lock before updating metadata.

    :arg batch_meta: An object of type :class:`NvDsBatchMeta`
    """

def nvds_acquire_obj_meta_from_pool(batch_meta: NvDsBatchMeta) -> NvDsObjectMeta:
    """Acquires :class:`NvDsObjectMeta` from the object meta pool. User must acquire
    the object meta from the object meta pool to fill object metadata.

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` from which
    :class:`NvDsObjectMeta` will be acquired

    :returns: Acquired :class:`NvDsObjectMeta` object from object meta pool
    """

def nvds_acquire_user_meta_from_pool(batch_meta: NvDsBatchMeta) -> NvDsUserMeta:
    """Acquires NvDsUserMeta from the user meta pool. User must acquire the user meta
    from the user meta pool to fill user metadata.

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` from which
    :class:`NvDsUserMeta` will be acquired
    """

def nvds_add_classifier_meta_to_object(
    obj_meta: NvDsObjectMeta, classifier_meta: NvDsClassifierMeta
) -> None:
    """After acquiring and filling classifier metadata user must add it to the object
    metadata with this API.

    :arg obj_meta: An object of type :class:`NvDsObjectMeta` to which classifier_meta
    will be attached.
    :arg classifier_meta: An object of type :class:`NvDsClassifierMeta` acquired from
    classifier_meta_pool present in :class:`NvDsBatchMeta`.
    """

def nvds_add_display_meta_to_frame(
    frame_meta: NvDsFrameMeta, display_meta: NvDsDisplayMeta
) -> None:
    """After acquiring and filling classifier metadata user must add it to the frame
    metadata with this API.

    :arg frame_meta: An object of type :class:`NvDsFrameMeta` to which display_meta
    will be attached.
    :arg display_meta: An object of type :class:`NvDsDisplayMeta` acquired from
    display_meta_pool present in :class:`NvDsBatchMeta`.
    """

def nvds_add_frame_meta_to_batch(
    batch_meta: NvDsBatchMeta, frame_meta: NvDsFrameMeta
) -> None:
    """After acquiring and filling frame metadata, user must add it to the batch
    metadata with this API.

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` to which frame_meta
    will be attached.
    :arg frame_meta: An object of type :class:`NvDsFrameMeta` acquired from
    frame_meta_pool present in :class:`NvDsBatchMeta`
    """

def nvds_add_label_info_meta_to_classifier(
    classifier_meta: NvDsClassifierMeta, label_info_meta: NvDsLabelInfo
) -> None:
    """After acquiring and filling labelinfo metadata user must add it to the
    classifier metadata with this API.

    :arg classifier_meta: An object of type :class:`NvDsClassifierMeta` to which
    label_info_meta will be attached.
    :arg label_info_meta: An object of type :class:`NvDsLabelInfo` acquired from
    label_info_meta_pool present in :class:`NvDsBatchMeta`.
    """

def nvds_add_obj_meta_to_frame(
    frame_meta: NvDsFrameMeta, obj_meta: NvDsObjectMeta, obj_parent: NvDsObjectMeta
) -> None:
    """After acquiring and filling object metadata user must add it to the frame
    metadata with this API.

    :arg frame_meta: An object of type :class:`NvDsFrameMeta` to which obj_meta will
    be attached.
    :arg obj_meta: An object of type :class:`NvDsObjectMeta` acquired from
    obj_meta_pool present in :class:`NvDsBatchMeta`.
    :arg obj_parent: A parent object of type :class:`NvDsObjectMeta`. This will set
    the parent object's to obj_meta.
    """

def nvds_add_user_meta_to_batch(
    batch_meta: NvDsBatchMeta, user_meta: NvDsUserMeta
) -> None:
    """After acquiring and filling user metadata user must add it to batch metadata
    if required at batch level with this API.

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` to which user_meta will
    be attached.
    :arg user_meta: An object of type :class:`NvDsUserMeta` acquired from
    user_meta_pool present in :class:`NvDsBatchMeta`.
    """

def nvds_add_user_meta_to_frame(
    frame_meta: NvDsFrameMeta, user_meta: NvDsUserMeta
) -> None:
    """After acquiring and filling user metadata user must add it to frame metadata
    if required at frame level with this API.

    :arg frame_meta: An object of type :class:`NvDsFrameMeta` to which user_meta will
    be attached.
    :arg user_meta: An object of type :class:`NvDsUserMeta` acquired from
    user_meta_pool present in :class:`NvDsBatchMeta`.
    """

def nvds_add_user_meta_to_obj(
    obj_meta: NvDsObjectMeta, user_meta: NvDsUserMeta
) -> None:
    """After acquiring and filling user metadata user must add it to object metadata
    if required at object level with this API.

    :arg obj_meta: An object of type :class:`NvDsObjectMeta` to which user_meta will
    be attached.
    :arg user_meta: An object of type :class:`NvDsUserMeta` acquired from
    user_meta_pool present :class:`NvDsBatchMeta`.
    """

def nvds_batch_meta_copy_func(
    data: capsule[NvDsBatchMeta], user_meta: typing.Any
) -> capsule:
    """Copy function to copy batch_meta. It is called when meta_data needs to copied
    / transformed from one buffer to other.
    meta_data and user_data are passed as arguments.

    :arg data: An object of type :class:`NvDsBatchMeta`
    :arg user_data: An object of user specific data

    :returns: An object that can be typecasted tot :class:`NvDsBatchMeta`
    """

def nvds_batch_meta_release_func(
    data: capsule[NvDsBatchMeta], user_data: capsule
) -> None:
    """batch_meta release function called when meta_data is going to be released.

    :arg data: An object of type :class:`NvDsBatchMeta`
    :arg user_data: An object of user specific data
    """

def nvds_clear_batch_user_meta_list(
    batch_meta: NvDsBatchMeta, meta_list: NvDsUserMetaList
) -> None:
    """Removes all the user metadata present in the batch metadata.

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` from which
    :class:`NvDsUserMetaList` needs to be cleared
    :arg meta_list: An object of type :class:`NvDsUserMetaList` which needs to be
    cleared
    """

NvDisplayMetaList: typing.TypeAlias = GList[NvDsDisplayMeta]

def nvds_clear_display_meta_list(
    frame_meta: NvDsFrameMeta, meta_list: NvDisplayMetaList
) -> None:
    """Removes all the display metadata present in the frame metadata.

    :arg frame_meta: An object of type :class:`NvDsFrameMeta` from which
    :class:`NvDisplayMetaList` needs to be cleared
    :arg meta_list: An object of type :class:`NvDisplayMetaList` which needs to be
    cleared
    """

NvDsFrameMetaList: typing.TypeAlias = GList[NvDsFrameMeta]

def nvds_clear_frame_meta_list(
    batch_meta: NvDsBatchMeta, meta_list: NvDsFrameMetaList
) -> None:
    """Removes all the frame metadata present in the batch metadata.

    :arg batch_meta: An object type of :class:`NvDsBatchMeta` from which
    :class:`NvDsFrameMetaList` needs to be cleared
    :arg  meta_list: An object of type :class:`NvDsFrameMetaList` which needs to be
    cleared
    """

NvDsUserMetaList: typing.TypeAlias = GList[NvDsUserMeta]

def nvds_clear_frame_user_meta_list(
    frame_meta: NvDsFrameMeta, meta_list: NvDsUserMetaList
) -> None:
    """Removes all the user metadata present in the frame metadata.

    :arg frame_meta: An object of type :class:`NvDsFrameMeta` from which
    :class:`NvDsUserMetaList` needs to be cleared
    :arg meta_list: An object of type :class:`NvDsUserMetaList` which needs to be
    cleared
    """

def nvds_clear_meta_list(
    batch_meta: NvDsBatchMeta, meta_list: NvDsMetaList, meta_pool: NvDsMetaPool
) -> NvDsMetaList:
    """Removes all the metadata elements present in the given metadata list.

    :arg batch_meta: An object of type :class:`NvDsBatchMeta`
    :arg meta_list: An object of type :class:`NvDsMetaList` which needs to be cleared
    :arg meta_pool: An object of type :class:`NvDsMetaPool` to which list belongs to

    :returns: An object of updated meta list
    """

NvDsObjectMetaList: typing.TypeAlias = GList[NvDsObjectMeta]

def nvds_clear_obj_meta_list(
    frame_meta: NvDsFrameMeta, meta_list: NvDsObjectMetaList
) -> None:
    """Removes all the object metadata present in the frame metadata.

    :arg frame_meta: An object of type :class:`NvDsFrameMeta` from which
    :class:`NvDsObjectMetaList` needs to be cleared
    :arg meta_list: An object of type :class:`NvDsObjectMetaList` which needs to be
    cleared
    """

def nvds_clear_obj_user_meta_list(
    object_meta: NvDsObjectMeta, meta_list: NvDsUserMetaList
) -> None:
    """Removes all the user metadata present in the object metadata.

    :arg object_meta: An object of type :class:`NvDsObjectMeta` from which
    :class:`NvDsUserMetaList` needs to be cleared
    :arg meta_list: An object of type :class:`NvDsUserMetaList` which needs to be
    cleared
    """

def nvds_copy_batch_user_meta_list(
    src_user_meta_list: NvDsUserMetaList, dst_batch_meta: NvDsBatchMeta
) -> None:
    """Deep copy of src_user_meta_list to user meta list present in the dst_batch_meta.

    :arg src_user_meta_list: An obect of type :class:`NvDsUserMetaList`
    :arg dst_batch_meta: An object of type :class:`NvDsBatchMeta`
    """

def nvds_copy_display_meta_list(
    src_display_meta: NvDisplayMetaList, dst_frame_meta: NvDsFrameMeta
) -> None:
    """Deep copy of src_display_meta_list to display meta list present in the
    dst_frame_meta.

    :arg src_display_meta_list: An object of type :class:`NvDisplayMetaList`
    :arg dst_frame_meta: An object of type :class:`NvDsFrameMeta`
    """

def nvds_copy_frame_meta_list(
    src_frame_meta_list: NvDsFrameMetaList, dst_batch_meta: NvDsBatchMeta
) -> None:
    """Deep copy of src_frame_meta_list to frame meta list present in the
    dst_batch_meta.

    :arg src_frame_meta_list: An object of type :class:`NvDsFrameMetaList`
    :arg dst_batch_meta: An object of type :class:`NvDsBatchMeta`
    """

def nvds_copy_frame_user_meta_list(
    src_user_meta_list: NvDsUserMetaList, dst_frame_meta: NvDsFrameMeta
) -> None:
    """Deep copy of src_user_meta_list to user meta list present in the dst_frame_meta.

    :arg src_user_meta_list: An object of type :class:`NvDsUserMetaList`
    :arg dst_frame_meta: An object of type :class:`NvDsFrameMeta`
    """

def nvds_copy_obj_meta_list(
    src_obj_meta_list: NvDsObjectMetaList, dst_object_meta: NvDsFrameMeta
) -> None:
    """Deep copy of src_obj_meta_list to frame meta list present in the dst_frame_meta.

    :arg src_obj_meta_list: An object of type :class:`NvDsObjectMetaList`
    :arg dst_frame_meta: An object of type :class:`NvDsFrameMeta`
    """

def nvds_create_batch_meta(max_batch_size: int) -> NvDsBatchMeta:
    """Creates a :class:`NvDsBatchMeta` of given batch size.

    :arg max_batch_size: maximum number of frames those can be present in the batch
    :returns: Allocated :class:`NvDsBatchMeta` object
    """

def nvds_destroy_batch_meta(batch_meta: NvDsBatchMeta) -> int:
    """Deletes/Releases given :class:`NvDsBatchMeta` batch_meta object.

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` to be deleted/destroyed
    after use
    """

def nvds_get_current_metadata_info(batch_meta: NvDsBatchMeta) -> int:
    """Debug function to get current metadata info.

    :arg batch_meta: An object of type :class:`NvDsBatchMeta`
    """

def nvds_get_nth_frame_meta(
    frame_meta_list: GList[NvDsFrameMeta], index: int
) -> NvDsFrameMeta:
    """Retrieve the :class:`NvDsFrameMeta` object of the frame at index.

    :arg frame_meta_list: A list of objects of type :class:`NvDsFrameMeta`
    :arg index: index at which :class:`NvDsFrameMeta` object needs to be accessed.

    :returns:  An object of type :class:`NvDsFrameMeta` from frame_meta_list
    """

def nvds_get_user_meta_type(meta_descriptor: str) -> NvDsMetaType:
    """Generates a unique user metadata type from the given string describing user
    specific metadata.

    :arg meta_descriptor: A string object describing metadata.
    The format of the string should be specified as below:
        ORG_NAME.COMPONENT_NAME.METADATA_DESCRIPTION.

        e.g. (NVIDIA.NVINFER.TENSOR_METADATA)
    """

def nvds_release_meta_lock(batch_meta: NvDsBatchMeta) -> None:
    """Release lock after updating metadata.

    :arg batch_meta: An object of type :class:`NvDsBatchMeta`
    """

def nvds_remove_classifier_meta_from_obj(
    obj_meta: NvDsObjectMeta, classifier_meta: NvDsClassifierMeta
) -> None:
    """Removes given classifier meta from object metadata.

    :arg obj_meta: An object of type :class:`NvDsObjectMeta` from which
    classifier_meta is to be removed.
    :arg classifier_meta: An object of type :class:`NvDsClassifierMeta` to be removed
    from obj_meta.
    """

def nvds_remove_display_meta_from_frame(
    frame_meta: NvDsFrameMeta, display_meta: NvDsDisplayMeta
) -> None:
    """Removes given display meta from frame metadata.

    :arg frame_meta: An object of type :class:`NvDsFrameMeta` from which display_meta
    is to be removed.
    :arg display_meta: An object of type :class:`NvDsDisplayMeta` to be removed from
    frame_meta.
    """

def nvds_remove_frame_meta_from_batch(
    batch_meta: NvDsBatchMeta, frame_meta: NvDsFrameMeta
) -> None:
    """Removes given frame meta from the batch metadata.

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` from which frame_meta
    is to be removed.
    :arg frame_meta: A object of type :class:`NvDsFrameMeta` to be removed from
    batch_meta.
    """

def nvds_remove_label_info_meta_from_classifier(
    classifier_meta: NvDsClassifierMeta, label_info_meta: NvDsLabelInfo
) -> None:
    """Removes given labelinfo meta from the classifier metadata.

    :arg classifier_meta: An object of type :class:`NvDsClassifierMeta` from which
    label_info_meta is to be removed.
    :arg label_info_meta: An object of type :class:`NvDsLabelInfo` to be removed from
    classifier_meta.
    """

def nvds_remove_obj_meta_from_frame(
    frame_meta: NvDsFrameMeta, obj_meta: NvDsObjectMeta
) -> None:
    """Removes given object meta from the frame metadata.

    :arg frame_meta: An object of type :class:`NvDsFrameMeta` from which obj_meta is
    to be removed.
    :arg obj_meta: An object of type :class:`NvDsObjectMeta` to be removed from
    frame_meta.
    """

def nvds_remove_user_meta_from_batch(
    batch_meta: NvDsBatchMeta, user_meta: NvDsUserMeta
) -> None:
    """Removes given user metadata from the batch metadata.

    :arg batch_meta: An object of type :class:`NvDsBatchMeta` from which user_meta
    is to be removed.
    :arg user_meta: An object of type :class:`NvDsUserMeta` to be removed from
    batch_meta.

    :returns: Acquired :class:`NvDsUserMeta` object from user meta pool
    """

def nvds_remove_user_meta_from_frame(
    frame_meta: NvDsFrameMeta, user_meta: NvDsUserMeta
) -> None:
    """Removes given user metadata from the frame metadata.

    :arg frame_meta: An object of type :class:`NvDsFrameMeta` from which user_meta is
    to be removed.
    :arg user_meta: An object of type :class:`NvDsUserMeta` to be removed from
    frame_meta.
    """

def nvds_remove_user_meta_from_object(
    obj_meta: NvDsObjectMeta, user_meta: NvDsUserMeta
) -> None:
    """Removes given user metadata from the object metadata.

    :arg obj_meta: An object of type :class:`NvDsObjectMeta` from which user_meta is
    to be removed.
    :arg user_meta: An object of type :class:`NvDsUserMeta` to be removed from obj_meta.
    """

def register_user_copyfunc(
    arg0: typing.Callable[[typing.Any, typing.Any], typing.Any],
) -> None: ...
def register_user_releasefunc(
    arg0: typing.Callable[[typing.Any, typing.Any], None],
) -> None: ...
def set_user_copyfunc(
    arg0: NvDsUserMeta,
    arg1: typing.Callable[[typing.Any, typing.Any], typing.Any],
) -> None: ...
def set_user_releasefunc(
    arg0: NvDsUserMeta,
    arg1: typing.Callable[[typing.Any, typing.Any], None],
) -> None: ...
def strdup(arg0: int) -> int: ...
def strdup2str(arg0: int) -> str: ...
def unmap_nvds_buf_surface(gst_buffer: int, batchID: int) -> None:
    """This function unmaps the NvBufSurface of the given Gst buffer and batch id,
    if previously mapped. For Jetson, a matching call to this function must be made for
    every call to :py:func:`get_nvds_buf_surface`.

    The array can no longer be accessed after this call, as the memory is released.

    :arg gst_buffer: address of the Gstbuffer which contains `NvBufSurface`
    :arg batchID: batch_id of the frame to be processed. This indicates the frame's
    index within :class:`NvBufSurface`
    """

def unset_callback_funcs() -> None: ...
def user_copyfunc(
    meta: NvDsUserMeta,
    func: typing.Callable[[typing.Any, typing.Any], typing.Any],
) -> None:
    """Set copy callback function of given :class:`NvDsUserMeta` object.

    :arg meta: :class:`NvDsUserMeta` of which to set copy function
    :arg func: User-written copy function
    """

def user_releasefunc(
    meta: NvDsUserMeta,
    func: typing.Callable[[typing.Any, typing.Any], None],
) -> None:
    """Set release callback function of given :class:`NvDsUserMeta` object.

    :arg meta: :class:`NvDsUserMeta` of which to set release function
    :arg func: User-written release function
    """

BOTH_HEAD: NvOSD_Arrow_Head_Direction  # value = NvOSD_Arrow_Head_Direction.BOTH_HEAD
END_HEAD: NvOSD_Arrow_Head_Direction  # value = NvOSD_Arrow_Head_Direction.END_HEAD
FLOAT: NvDsInferDataType  # value = NvDsInferDataType.FLOAT
HALF: NvDsInferDataType  # value = NvDsInferDataType.HALF
INSIDE_AISLE_360D: ROI_STATUS_360D  # value = ROI_STATUS_360D.INSIDE_AISLE_360D
INT32: NvDsInferDataType  # value = NvDsInferDataType.INT32
INT8: NvDsInferDataType  # value = NvDsInferDataType.INT8
MODE_CPU: NvOSD_Mode  # value = NvOSD_Mode.MODE_CPU
MODE_GPU: NvOSD_Mode  # value = NvOSD_Mode.MODE_GPU
MODE_NONE: NvOSD_Mode  # value = NvOSD_Mode.MODE_NONE
NVBUF_COLOR_FORMAT_ABGR: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_ABGR
)
NVBUF_COLOR_FORMAT_ARGB: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_ARGB
)
NVBUF_COLOR_FORMAT_BGR: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_BGR
)
NVBUF_COLOR_FORMAT_BGRA: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_BGRA
)
NVBUF_COLOR_FORMAT_BGRx: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_BGRx
)
NVBUF_COLOR_FORMAT_GRAY8: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_GRAY8
)
NVBUF_COLOR_FORMAT_INVALID: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_INVALID
NVBUF_COLOR_FORMAT_LAST: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_LAST
)
NVBUF_COLOR_FORMAT_NV12: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12
)
NVBUF_COLOR_FORMAT_NV12_10LE: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE
NVBUF_COLOR_FORMAT_NV12_10LE_2020: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE_2020
NVBUF_COLOR_FORMAT_NV12_10LE_709: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE_709
NVBUF_COLOR_FORMAT_NV12_10LE_709_ER: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE_709_ER
NVBUF_COLOR_FORMAT_NV12_10LE_ER: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_10LE_ER
NVBUF_COLOR_FORMAT_NV12_12LE: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_12LE
NVBUF_COLOR_FORMAT_NV12_2020: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_2020
NVBUF_COLOR_FORMAT_NV12_709: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_709
NVBUF_COLOR_FORMAT_NV12_709_ER: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_709_ER
NVBUF_COLOR_FORMAT_NV12_ER: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV12_ER
NVBUF_COLOR_FORMAT_NV21: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV21
)
NVBUF_COLOR_FORMAT_NV21_ER: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_NV21_ER
NVBUF_COLOR_FORMAT_RGB: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_RGB
)
NVBUF_COLOR_FORMAT_RGBA: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_RGBA
)
NVBUF_COLOR_FORMAT_RGBx: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_RGBx
)
NVBUF_COLOR_FORMAT_SIGNED_R16G16: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_SIGNED_R16G16
NVBUF_COLOR_FORMAT_UYVY: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_UYVY
)
NVBUF_COLOR_FORMAT_UYVY_ER: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_UYVY_ER
NVBUF_COLOR_FORMAT_VYUY: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_VYUY
)
NVBUF_COLOR_FORMAT_VYUY_ER: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_VYUY_ER
NVBUF_COLOR_FORMAT_YUV420: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420
)
NVBUF_COLOR_FORMAT_YUV420_2020: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420_2020
NVBUF_COLOR_FORMAT_YUV420_709: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420_709
NVBUF_COLOR_FORMAT_YUV420_709_ER: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420_709_ER
NVBUF_COLOR_FORMAT_YUV420_ER: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV420_ER
NVBUF_COLOR_FORMAT_YUV444: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUV444
)
NVBUF_COLOR_FORMAT_YUYV: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUYV
)
NVBUF_COLOR_FORMAT_YUYV_ER: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YUYV_ER
NVBUF_COLOR_FORMAT_YVU420: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YVU420
)
NVBUF_COLOR_FORMAT_YVU420_ER: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YVU420_ER
NVBUF_COLOR_FORMAT_YVYU: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YVYU
)
NVBUF_COLOR_FORMAT_YVYU_ER: NvBufSurfaceColorFormat  # value =
# NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_YVYU_ER
NVBUF_COLOR_FORMAT_xBGR: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_xBGR
)
NVBUF_COLOR_FORMAT_xRGB: (
    NvBufSurfaceColorFormat  # value = NvBufSurfaceColorFormat.NVBUF_COLOR_FORMAT_xRGB
)
NVBUF_LAYOUT_BLOCK_LINEAR: (
    NvBufSurfaceLayout  # value = NvBufSurfaceLayout.NVBUF_LAYOUT_BLOCK_LINEAR
)
NVBUF_LAYOUT_PITCH: NvBufSurfaceLayout  # value = NvBufSurfaceLayout.NVBUF_LAYOUT_PITCH
NVBUF_MAP_READ: (
    NvBufSurfaceMemMapFlags  # value = NvBufSurfaceMemMapFlags.NVBUF_MAP_READ
)
NVBUF_MAP_READ_WRITE: (
    NvBufSurfaceMemMapFlags  # value = NvBufSurfaceMemMapFlags.NVBUF_MAP_READ_WRITE
)
NVBUF_MAP_WRITE: (
    NvBufSurfaceMemMapFlags  # value = NvBufSurfaceMemMapFlags.NVBUF_MAP_WRITE
)
NVBUF_MEM_CUDA_DEVICE: (
    NvBufSurfaceMemType  # value = NvBufSurfaceMemType.NVBUF_MEM_CUDA_DEVICE
)
NVBUF_MEM_CUDA_PINNED: (
    NvBufSurfaceMemType  # value = NvBufSurfaceMemType.NVBUF_MEM_CUDA_PINNED
)
NVBUF_MEM_CUDA_UNIFIED: (
    NvBufSurfaceMemType  # value = NvBufSurfaceMemType.NVBUF_MEM_CUDA_UNIFIED
)
NVBUF_MEM_DEFAULT: NvBufSurfaceMemType  # value = NvBufSurfaceMemType.NVBUF_MEM_DEFAULT
NVBUF_MEM_HANDLE: NvBufSurfaceMemType  # value = NvBufSurfaceMemType.NVBUF_MEM_HANDLE
NVBUF_MEM_SURFACE_ARRAY: (
    NvBufSurfaceMemType  # value = NvBufSurfaceMemType.NVBUF_MEM_SURFACE_ARRAY
)
NVBUF_MEM_SYSTEM: NvBufSurfaceMemType  # value = NvBufSurfaceMemType.NVBUF_MEM_SYSTEM
NVDSINFER_SEGMENTATION_META: (
    NvDsMetaType  # value = NvDsMetaType.NVDSINFER_SEGMENTATION_META
)
NVDSINFER_TENSOR_OUTPUT_META: (
    NvDsMetaType  # value = NvDsMetaType.NVDSINFER_TENSOR_OUTPUT_META
)
NVDS_AUDIO_BATCH_META: NvDsMetaType  # value = NvDsMetaType.NVDS_AUDIO_BATCH_META
NVDS_AUDIO_FRAME_META: NvDsMetaType  # value = NvDsMetaType.NVDS_AUDIO_FRAME_META
NVDS_BATCH_GST_META: GstNvDsMetaType  # value = GstNvDsMetaType.NVDS_BATCH_GST_META
NVDS_BATCH_META: NvDsMetaType  # value = NvDsMetaType.NVDS_BATCH_META
NVDS_CLASSIFIER_META: NvDsMetaType  # value = NvDsMetaType.NVDS_CLASSIFIER_META
NVDS_CROP_IMAGE_META: NvDsMetaType  # value = NvDsMetaType.NVDS_CROP_IMAGE_META
NVDS_DECODER_GST_META: GstNvDsMetaType  # value = GstNvDsMetaType.NVDS_DECODER_GST_META
NVDS_DEWARPER_GST_META: (
    GstNvDsMetaType  # value = GstNvDsMetaType.NVDS_DEWARPER_GST_META
)
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
NVDS_LATENCY_MEASUREMENT_META: (
    NvDsMetaType  # value = NvDsMetaType.NVDS_LATENCY_MEASUREMENT_META
)
NVDS_OBEJCT_TYPE_FORCE32: (
    NvDsObjectType  # value = NvDsObjectType.NVDS_OBEJCT_TYPE_FORCE32
)
NVDS_OBJECT_TYPE_BAG: NvDsObjectType  # value = NvDsObjectType.NVDS_OBJECT_TYPE_BAG
NVDS_OBJECT_TYPE_BICYCLE: (
    NvDsObjectType  # value = NvDsObjectType.NVDS_OBJECT_TYPE_BICYCLE
)
NVDS_OBJECT_TYPE_CUSTOM: (
    NvDsObjectType  # value = NvDsObjectType.NVDS_OBJECT_TYPE_CUSTOM
)
NVDS_OBJECT_TYPE_FACE: NvDsObjectType  # value = NvDsObjectType.NVDS_OBJECT_TYPE_FACE
NVDS_OBJECT_TYPE_FACE_EXT: (
    NvDsObjectType  # value = NvDsObjectType.NVDS_OBJECT_TYPE_FACE_EXT
)
NVDS_OBJECT_TYPE_PERSON: (
    NvDsObjectType  # value = NvDsObjectType.NVDS_OBJECT_TYPE_PERSON
)
NVDS_OBJECT_TYPE_PERSON_EXT: (
    NvDsObjectType  # value = NvDsObjectType.NVDS_OBJECT_TYPE_PERSON_EXT
)
NVDS_OBJECT_TYPE_RESERVED: (
    NvDsObjectType  # value = NvDsObjectType.NVDS_OBJECT_TYPE_RESERVED
)
NVDS_OBJECT_TYPE_ROADSIGN: (
    NvDsObjectType  # value = NvDsObjectType.NVDS_OBJECT_TYPE_ROADSIGN
)
NVDS_OBJECT_TYPE_UNKNOWN: (
    NvDsObjectType  # value = NvDsObjectType.NVDS_OBJECT_TYPE_UNKNOWN
)
NVDS_OBJECT_TYPE_VEHICLE: (
    NvDsObjectType  # value = NvDsObjectType.NVDS_OBJECT_TYPE_VEHICLE
)
NVDS_OBJECT_TYPE_VEHICLE_EXT: (
    NvDsObjectType  # value = NvDsObjectType.NVDS_OBJECT_TYPE_VEHICLE_EXT
)
NVDS_OBJ_META: NvDsMetaType  # value = NvDsMetaType.NVDS_OBJ_META
NVDS_OPTICAL_FLOW_META: NvDsMetaType  # value = NvDsMetaType.NVDS_OPTICAL_FLOW_META
NVDS_PAYLOAD_CUSTOM: NvDsPayloadType  # value = NvDsPayloadType.NVDS_PAYLOAD_CUSTOM
NVDS_PAYLOAD_DEEPSTREAM: (
    NvDsPayloadType  # value = NvDsPayloadType.NVDS_PAYLOAD_DEEPSTREAM
)
NVDS_PAYLOAD_DEEPSTREAM_MINIMAL: (
    NvDsPayloadType  # value = NvDsPayloadType.NVDS_PAYLOAD_DEEPSTREAM_MINIMAL
)
NVDS_PAYLOAD_FORCE32: NvDsPayloadType  # value = NvDsPayloadType.NVDS_PAYLOAD_FORCE32
NVDS_PAYLOAD_META: NvDsMetaType  # value = NvDsMetaType.NVDS_PAYLOAD_META
NVDS_PAYLOAD_RESERVED: NvDsPayloadType  # value = NvDsPayloadType.NVDS_PAYLOAD_RESERVED
NVDS_RESERVED_GST_META: (
    GstNvDsMetaType  # value = GstNvDsMetaType.NVDS_RESERVED_GST_META
)
NVDS_RESERVED_META: NvDsMetaType  # value = NvDsMetaType.NVDS_RESERVED_META
NVDS_START_USER_META: NvDsMetaType  # value = NvDsMetaType.NVDS_START_USER_META
NVDS_TRACKER_PAST_FRAME_META: (
    NvDsMetaType  # value = NvDsMetaType.NVDS_TRACKER_PAST_FRAME_META
)
NVDS_USER_META: NvDsMetaType  # value = NvDsMetaType.NVDS_USER_META
ROI_ENTRY_360D: ROI_STATUS_360D  # value = ROI_STATUS_360D.ROI_ENTRY_360D
ROI_EXIT_360D: ROI_STATUS_360D  # value = ROI_STATUS_360D.ROI_EXIT_360D
START_HEAD: NvOSD_Arrow_Head_Direction  # value = NvOSD_Arrow_Head_Direction.START_HEAD
__version__: str = "1.1.8"

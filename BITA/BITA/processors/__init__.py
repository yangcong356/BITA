from BITA.processors.base_processor import BaseProcessor

from BITA.processors.bita_processors import (
    BITAImageTrainProcessor,
    BITAImageEvalProcessor,
    BITACaptionProcessor,
)

from BITA.common.registry import Registry

__all__ = [
    "BaseProcessor",
    "BITAImageTrainProcessor",
    "BITAImageEvalProcessor",
    "BITACaptionProcessor",
]

def load_processor(name, cfg=None):
    """
    Example

    >>> processor = load_processor("alpro_video_train", cfg=None)
    """
    processor = Registry.get_processor_class(name).from_config(cfg)

    return processor
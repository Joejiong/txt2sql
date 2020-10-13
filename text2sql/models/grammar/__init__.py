# -*- coding:utf8 -*-
"""grammar model"""

from collections import namedtuple

DecoderInputsWrapper = namedtuple("DecoderInputsWrapper", "input action gmr_mask")
DecoderDynamicVocab = namedtuple("DecoderDynamicVocab",
                                 "table table_len column column_len value value_len column2table_mask")

from text2sql.models.grammar.nets import grammar_output
from text2sql.models.grammar.infer_decoder import GrammarInferDecoder
from text2sql.models.grammar.dynamic_decode import decode_with_grammar


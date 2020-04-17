# This code is adapted from LLK/scratch-parser from the Massachusetts Institute of Technology.
# It's a combination of https://github.com/LLK/scratch-parser/blob/master/lib/sb3_definitions.json
# and https://github.com/LLK/scratch-parser/blob/master/lib/sb3_schema.json

# This code is thus governed by the BSD-3 Clause "Revised" License:
# https://github.com/LLK/scratch-parser/blob/master/LICENSE


# Copyright (c) 2016, Massachusetts Institute of Technology
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


sb3_schema = {
    "$id": "https://scratch.mit.edu/sb3_schema.json",
    "$schema": "http://json-schema.org/schema#",
    "description": "Scratch 3.0 Project Schema",
    "type": "object",
    "properties": {
        "meta": {
            "type": "object",
            "properties": {
                "semver": {
                    "type": "string",
                    "pattern": "^(3\\.[0-9]+\\.[0-9]+)$"
                },
                "vm": {
                    "type": "string",
                    "pattern": "^([0-9]+\\.[0-9]+\\.[0-9]+)($|-)"
                },
                "agent": {
                    "type": "string"
                }
            },
            "required": [
                "semver"
            ]
        },
        "targets": {
            "type": "array",
            "items": [
                {
                    "allOf": [
                        {"$ref": "#/definitions/stage" },
                        {"$ref": "#/definitions/target"}
                    ]
                }
            ],
            "additionalItems": {
                "allOf": [
                    {"$ref": "#/definitions/sprite"},
                    {"$ref": "#/definitions/target"}
                ]
            }
        }
    },
    "required": [
        "meta",
        "targets"
    ],
    "definitions": {
        "optionalString": {
            "oneOf": [
                {"type": "string"},
                {"type": "null"}
            ]
        },
        "optionalNumber": {
            "oneOf": [
                {"type": "number"},
                {"type": "null"}
            ]
        },
        "boolOrOptBoolString": {
            "oneOf": [
                {"type": "string",
                 "enum": ["true", "false", "null"]},
                {"type": "boolean"},
                {"type": "null"}
            ]
        },
        "stringOrNumber": {
            "oneOf": [
                {"type": "string"},
                {"type": "number"}
            ]
        },
        "scalarVal": {
            "oneOf": [
                {"$ref":"#/definitions/stringOrNumber"},
                {"type": "boolean"}
            ]
        },
        "assetId": {
            "type": "string",
            "pattern": "^[a-fA-F0-9]{32}$"
        },
        "costume": {
            "type": "object",
            "properties": {
                "assetId": { "$ref": "#/definitions/assetId"},
                "bitmapResolution": {
                    "type": "integer"
                },
                "dataFormat": {
                    "type": "string",
                    "enum": ["png", "svg", "jpeg", "jpg", "bmp", "gif"]
                },
                "md5ext": {
                    "type": "string",
                    "pattern": "^[a-fA-F0-9]{32}\\.[a-zA-Z]+$"
                },
                "name": {
                    "type": "string"
                },
                "rotationCenterX": {
                    "type": "number",
                    "description": "This property is not required, but is highly recommended."
                },
                "rotationCenterY": {
                    "type": "number",
                    "description": "This property is not required, but is highly recommended."
                }
            },
            "required": [
                "assetId",
                "dataFormat",
                "name"
            ]
        },
        "sound": {
            "type": "object",
            "properties": {
                "assetId": { "$ref": "#/definitions/assetId"},
                "dataFormat": {
                    "type": "string",
                    "enum": ["wav", "wave", "mp3"]
                },
                "md5ext": {
                    "type": "string",
                    "pattern": "^[a-fA-F0-9]{32}\\.[a-zA-Z0-9]+$"
                },
                "name": {
                    "type": "string"
                },
                "rate": {
                    "type": "integer"
                },
                "sampleCount": {
                    "type": "integer"
                }
            },
            "required": [
                "assetId",
                "dataFormat",
                "name"
            ]
        },
        "scalar_variable": {
            "type": "array",
            "items": [
                {"type": "string", "description": "name of the variable"},
                {"$ref":"#/definitions/scalarVal", "description": "value of the variable"}
            ],
            "additionalItems": {"type": "boolean", "enum": [True], "description": "Whether this is a cloud variable"},
            "maxItems": 3
        },
        "list": {
            "type": "array",
            "items": [
                {"type":"string", "description": "name of the list"},
                {
                    "type": "array",
                    "description": "contents of the list",
                    "items": {"$ref":"#/definitions/scalarVal"}
                }
            ],
            "additionalItems": False
        },
        "broadcast_message": {
            "type": "string",
            "description": "the message being broadcasted"
        },
        "num_primitive": {
            "type": "array",
            "items": [
                {
                    "type": "number",
                    "enum": [4,5,6,7,8]
                },
                {"$ref":"#/definitions/stringOrNumber"}
            ],
            "additionalItems": False
        },
        "color_primitive": {
            "type": "array",
            "items": [
                {
                    "type": "number",
                    "enum": [9]
                },
                {
                    "type": "string",
                    "pattern": "^#[a-fA-F0-9]{6}$"
                }
            ],
            "additionalItems": False
        },
        "text_primitive": {
            "type": "array",
            "items": [
                {
                    "type": "number",
                    "enum": [10]
                },
                {"$ref":"#/definitions/stringOrNumber"}
            ],
            "additionalItems": False
        },
        "broadcast_primitive": {
            "type": "array",
            "items": [
                {
                    "type": "number",
                    "enum": [11]
                },
                {"type": "string", "description": "broadcast message"},
                {"type": "string", "description": "broadcast message id"}
            ],
            "additionalItems": False
        },
        "variable_primitive": {
            "type": "array",
            "items": [
                {
                    "type": "number",
                    "enum": [12]
                },
                {"type": "string", "description": "variable name"},
                {"type": "string", "description": "variable id"}
            ],
            "additionalItems": {
                "type": "number"
            },
            "minItems": 3,
            "maxItems": 5
        },
        "list_primitive": {
            "type": "array",
            "items": [
                {
                    "type": "number",
                    "enum": [13]
                },
                {"type": "string", "description": "list name"},
                {"type": "string", "description": "list id"}
            ],
            "additionalItems": {
                "type": "number"
            },
            "minItems": 3,
            "maxItems": 5
        },
        "topLevelPrimitive": {
            "oneOf": [
                {"$ref":"#/definitions/variable_primitive"},
                {"$ref":"#/definitions/list_primitive"}
            ]
        },
        "inputPrimitive": {
            "oneOf": [
                {"$ref":"#/definitions/num_primitive"},
                {"$ref":"#/definitions/color_primitive"},
                {"$ref":"#/definitions/text_primitive"},
                {"$ref":"#/definitions/broadcast_primitive"},
                {"$ref":"#/definitions/variable_primitive"},
                {"$ref":"#/definitions/list_primitive"}
            ]
        },
        "block": {
            "type": "object",
            "properties": {
                "opcode": {
                    "type": "string"
                },
                "comment": {
                    "type": "string"
                },
                "inputs": {
                    "type": "object",
                    "additionalProperties": {
                        "type": "array",
                        "items": [
                            {
                                "type":"number",
                                "enum":[1,2,3],
                                "description": "1 = unobscured shadow, 2 = no shadow, 3 = obscured shadow"
                            }
                        ],
                        "additionalItems": {
                            "oneOf": [
                                {"$ref":"#/definitions/optionalString"},
                                {"$ref":"#/definitions/inputPrimitive"}
                            ]
                        }
                    }
                },
                "fields": {
                    "type": "object"
                },
                "next": {"$ref":"#/definitions/optionalString"},
                "topLevel": {
                    "type": "boolean"
                },
                "parent": {"$ref":"#/definitions/optionalString"},
                "shadow": {
                    "type": "boolean"
                },
                "x": {
                    "type": "number"
                },
                "y": {
                    "type": "number"
                },
                "mutation": {
                    "type": "object",
                    "properties": {
                        "tagName": {
                            "type": "string",
                            "enum": ["mutation"]
                        },
                        "children": {
                            "type": "array"
                        },
                        "proccode": {
                            "type": "string"
                        },
                        "argumentids": {
                            "type": "string"
                        },
                        "warp": {"$ref":"#/definitions/boolOrOptBoolString"},
                        "hasnext": {"$ref":"#/definitions/boolOrOptBoolString"}
                    }
                }
            },
            "required": [
                "opcode"
            ]
        },
        "comment": {
            "type": "object",
            "properties": {
                "blockId": {"$ref": "#/definitions/optionalString"},
                "text": {
                    "type": "string",
                    "maxLength": 8000
                },
                "minimized": {"type": "boolean"},
                "x": {"$ref": "#/definitions/optionalNumber"},
                "y": {"$ref": "#/definitions/optionalNumber"},
                "width": {"type": "number"},
                "height": {"type": "number"}
            },
            "required": [
                "text"
            ]
        },
        "stage": {
            "type": "object",
            "description": "Description of property (and/or property/value pairs) that are unique to the stage.",
            "properties": {
                "name": {
                    "type": "string",
                    "enum": ["Stage"]
                },
                "isStage": {
                    "type": "boolean",
                    "enum": [True]
                },
                "tempo": {
                    "type": "number"
                },
                "videoTransparency": {
                    "type": "number"
                },
                "videoState": {
                    "type": "string",
                    "enum": ["on", "off", "on-flipped"]
                },
                "layerOrder": {
                    "type": "integer",
                    "enum": [0],
                    "description": "The layer order of the stage should be 0, if specified."
                }
            },
            "required": [
                "name",
                "isStage"
            ]
        },
        "sprite": {
            "type": "object",
            "description": "Description of property (and/or property/value pairs) for sprites.",
            "properties": {
                "name": {
                    "type": "string",
                    "not": {"enum": ["_stage_"]}
                },
                "isStage": {
                    "type": "boolean",
                    "enum": [False]
                },
                "visible": {
                    "type": "boolean"
                },
                "x": {
                    "type": "number"
                },
                "y": {
                    "type": "number"
                },
                "size": {
                    "type": "number"
                },
                "direction": {
                    "type": "number"
                },
                "draggable": {
                    "type": "boolean"
                },
                "rotationStyle": {
                    "type": "string",
                    "enum": ["all around", "don't rotate", "left-right"]
                },
                "layerOrder": {
                    "type": "integer",
                    "minimum": 1,
                    "description": "The layer order of a sprite should be a positive number, if specified."
                }
            },
            "required": [
                "name",
                "isStage"
            ]
        },
        "target": {
            "type": "object",
            "description" : "Properties common to both Scratch 3.0 Stage and Sprite",
            "properties": {
                "currentCostume": {
                    "type": "integer",
                    "minimum": 0
                },
                "blocks": {
                    "type": "object",
                    "additionalProperties": {
                        "oneOf": [
                            {"$ref":"#/definitions/block"},
                            {"$ref":"#/definitions/topLevelPrimitive"}
                        ]
                    }
                },
                "variables": {
                    "type": "object",
                    "additionalProperties": {"$ref":"#/definitions/scalar_variable"}
                },
                "lists": {
                    "type": "object",
                    "additionalProperties": {"$ref":"#/definitions/list"}
                },
                "broadcasts": {
                    "type": "object",
                    "additionalProperties": {"$ref":"#/definitions/broadcast_message"}
                },
                "comments": {
                    "type": "object",
                    "additionalProperties": {"$ref": "#/definitions/comment"}
                },
                "costumes": {
                    "type": "array",
                    "items": {"$ref":"#/definitions/costume"},
                    "minItems": 1,
                    "uniqueItems": True
                },
                "sounds": {
                    "type": "array",
                    "items": {"$ref":"#/definitions/sound"},
                    "uniqueItems": True
                },
                "volume": {
                    "type": "number"
                }
            },
            "required": [
                "variables",
                "costumes",
                "sounds",
                "blocks"
            ]
        }
    }
}

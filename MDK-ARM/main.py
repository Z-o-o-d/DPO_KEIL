import json


def generate_keil_project_json(uv4_caller_path, uv4_path, prj_path, target_name, log_path):
    data = {
        "version": "2.0.0",
        "tasks": [
            {
                "label": "Rebuild Keil Project",
                "type": "shell",
                "command": uv4_caller_path,
                "args": [
                    "-o",
                    log_path,
                    "--uv4Path",
                    uv4_path,
                    "--prjPath",
                    prj_path,
                    "--targetName",
                    target_name,
                    "-c",
                    f"'{uv4_path} -r {prj_path} -j0 -t {target_name}'"
                ],
                "problemMatcher": {
                    "owner": "cpp",
                    "fileLocation": [
                        "relative",
                        "${workspaceFolder}"
                    ],
                    "pattern": [
                        {
                            "regexp": "^(..\\/[^:]+):(\\d+):\\s*(warning|error):\\s*(.*)$",
                            "file": 1,
                            "line": 2,
                            "severity": 3,
                            "message": 4
                        }
                    ]
                },
                "group": {
                    "kind": "build",
                    "isDefault": True
                }
            },
            {
                "label": "Build Keil Project",
                "type": "shell",
                "command": uv4_caller_path,
                "args": [
                    "-o",
                    log_path,
                    "--uv4Path",
                    uv4_path,
                    "--prjPath",
                    prj_path,
                    "--targetName",
                    target_name,
                    "-c",
                    f"'{uv4_path} -b {prj_path} -j0 -t {target_name}'"
                ],
                "problemMatcher": {
                    "owner": "cpp",
                    "fileLocation": [
                        "relative",
                        "${workspaceFolder}"
                    ],
                    "pattern": [
                        {
                            "regexp": "^(..\\/[^:]+):(\\d+):\\s*(warning|error):\\s*(.*)$",
                            "file": 1,
                            "line": 2,
                            "severity": 3,
                            "message": 4
                        }
                    ]
                },
                "group": {
                    "kind": "build",
                    "isDefault": False
                }
            },
            {
                "label": "Flash Keil Project",
                "type": "shell",
                "command": uv4_caller_path,
                "args": [
                    "-o",
                    log_path,
                    "--uv4Path",
                    uv4_path,
                    "--prjPath",
                    prj_path,
                    "--targetName",
                    target_name,
                    "-c",
                    f"'{uv4_path} -f {prj_path} -j0 -t {target_name}'"
                ],
                "problemMatcher": {
                    "owner": "cpp",
                    "fileLocation": [
                        "relative",
                        "${workspaceFolder}"
                    ],
                    "pattern": [
                        {
                            "regexp": "^(..\\/[^:]+):(\\d+):\\s*(warning|error):\\s*(.*)$",
                            "file": 1,
                            "line": 2,
                            "severity": 3,
                            "message": 4
                        }
                    ]
                },
                "group": {
                    "kind": "test",
                    "isDefault": True
                }
            }
        ]
    }
    return data


if __name__ == "__main__":
    # 修改这些路径以适应你的需求
    uv4_caller_path = "C:\\Users\\87407\\AppData\\Local\\Keil_v5\\Uv4Caller.exe"
    uv4_path = "C:\\Users\\87407\\AppData\\Local\\Keil_v5\\UV4\\UV4.exe"
    prj_path = "C:\\Users\\87407\\Keil_prj\\DPO_KEIL\\DPO_KEIL\\MDK-ARM\\DPO_KEIL.uvprojx"
    target_name = "DPO_KEIL"
    log_path = "C:\\Users\\87407\\Keil_prj\\DPO_KEIL\\DPO_KEIL\\MDK-ARM\\.vscode\\uv4.log"

    json_data = generate_keil_project_json(uv4_caller_path, uv4_path, prj_path, target_name, log_path)
    print(json.dumps(json_data, indent=4))
    
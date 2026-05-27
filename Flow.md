# pytest-CRUD-Framework - Architecture & Workflow

## System Architecture Overview

```mermaid
graph TB
    subgraph "Test Layer"
        A["tests/test_demo.py<br/>(Test Cases)"]
    end
    
    subgraph "Utilities Layer"
        B["src/utils/utils.py<br/>(HTTP Requests)"]
        C["src/helpers/common_verifications.py<br/>(Response Verification)"]
        D["src/helpers/payload_manager.py<br/>(Test Data)"]
    end
    
    subgraph "Configuration Layer"
        E["src/constants/API_CONSTANT.PY<br/>(Endpoints & Headers)"]
        F["conftest.py<br/>(pytest Config)"]
    end
    
    subgraph "External Services"
        G["JSONPlaceholder API<br/>(Mock Backend)"]
    end
    
    subgraph "Output"
        H["reports/<br/>(HTML Reports)"]
        I["Console Logs<br/>(Test Output)"]
    end
    
    A -->|Uses| B
    A -->|Uses| C
    A -->|Uses| D
    B -->|Uses| E
    D -->|Uses| E
    B -->|Makes Requests| G
    G -->|Returns Response| C
    C -->|Validates| H
    A -->|Configured by| F
    F -->|Generates| H
    F -->|Enables| I
```

---

## Test Execution Flow - CRUD Operations

```mermaid
sequenceDiagram
    participant Test as Test Case
    participant Utils as HTTP Utils
    participant Verify as Verification Helper
    participant API as JSONPlaceholder API
    participant Report as HTML Report
    
    Test->>Test: Load Constants (URLs, Headers)
    Test->>Test: Generate/Load Payload
    Test->>Utils: Call HTTP Method
    Utils->>API: Send HTTP Request
    API-->>Utils: Return Response
    Utils-->>Test: Response Object
    Test->>Verify: Verify Status Code
    Verify->>Verify: Check Response Code
    Verify-->>Test: Verification Result
    Test->>Verify: Verify JSON Response
    Verify->>Verify: Parse & Validate JSON
    Verify-->>Test: JSON Validation Result
    Test->>Report: Log Results
    Report->>Report: Generate HTML Report
```

---

## Detailed Component Interaction Flow

```mermaid
graph LR
    subgraph "Input"
        Input["Test Execution<br/>pytest command"]
    end
    
    subgraph "Configuration"
        Conf["conftest.py<br/>- Setup logging<br/>- Configure HTML report<br/>- Set report path"]
    end
    
    subgraph "Test Discovery"
        Discover["pytest discovers<br/>tests/test_demo.py"]
    end
    
    subgraph "Import Constants"
        Import["Load from<br/>src/constants/<br/>API_CONSTANT.PY"]
    end
    
    subgraph "HTTP Request Processing"
        Req1["Call HTTP Method<br/>from utils.py"]
        Req2["Use Headers from<br/>API_CONSTANT.PY"]
        Req3["Send Request to<br/>JSONPlaceholder API"]
    end
    
    subgraph "Response Processing"
        Resp1["Receive Response"]
        Resp2["Log Response Status"]
        Resp3["Parse JSON Response"]
    end
    
    subgraph "Verification"
        Ver1["Verify Status Code<br/>using common_verifications.py"]
        Ver2["Verify Headers"]
        Ver3["Verify JSON Keys<br/>& Structure"]
    end
    
    subgraph "Test Result"
        Result["PASS / FAIL<br/>Assertion"]
    end
    
    subgraph "Reporting"
        Report["Generate HTML Report<br/>with Test Summary<br/>reports/report_*.html"]
    end
    
    Input --> Conf
    Conf --> Discover
    Discover --> Import
    Import --> Req1
    Req1 --> Req2
    Req2 --> Req3
    Req3 --> Resp1
    Resp1 --> Resp2
    Resp2 --> Resp3
    Resp3 --> Ver1
    Ver1 --> Ver2
    Ver2 --> Ver3
    Ver3 --> Result
    Result --> Report
```

---

## CRUD Operations Test Flow

```mermaid
graph TD
    Start["Test Execution Starts"]
    
    subgraph "CREATE"
        C1["1. Generate User Payload<br/>payload_manager.py"]
        C2["2. POST Request<br/>to /users"]
        C3["3. Verify Status 201"]
        C4["4. Verify Response<br/>Contains User Data"]
    end
    
    subgraph "READ"
        R1["1. GET All Users<br/>from /users"]
        R2["2. Verify Status 200"]
        R3["3. Verify Response<br/>is List of Users"]
        R4["1. GET User by ID<br/>from /users/1"]
        R5["2. Verify Status 200"]
        R6["3. Verify Response<br/>Contains User Object"]
    end
    
    subgraph "UPDATE"
        U1["1. Load Update Payload<br/>payload_manager.py"]
        U2["2. PUT Request<br/>to /users/1"]
        U3["3. Verify Status 200"]
        U4["4. Verify Response<br/>Contains Updated Data"]
    end
    
    subgraph "DELETE"
        D1["1. DELETE Request<br/>to /users/1"]
        D2["2. Verify Status 200"]
        D3["3. Verify User Deleted"]
    end
    
    Start --> C1
    C1 --> C2
    C2 --> C3
    C3 --> C4
    C4 --> R1
    R1 --> R2
    R2 --> R3
    R3 --> R4
    R4 --> R5
    R5 --> R6
    R6 --> U1
    U1 --> U2
    U2 --> U3
    U3 --> U4
    U4 --> D1
    D1 --> D2
    D2 --> D3
    D3 --> End["All Tests Complete<br/>Report Generated"]
    
    style C1 fill:#e1f5e1
    style R1 fill:#e1f5ff
    style U1 fill:#ffe1f5
    style D1 fill:#ffe1e1
```

---

## Data Flow - Request to Response

```mermaid
graph LR
    subgraph "Request Creation"
        RC["Request Components:<br/>- Endpoint URL<br/>- HTTP Method<br/>- Headers<br/>- Body/Payload"]
    end
    
    subgraph "HTTP Request"
        HR["requests library<br/>sends to<br/>JSONPlaceholder API"]
    end
    
    subgraph "Server Processing"
        SP["API processes request<br/>and returns response<br/>with status code"]
    end
    
    subgraph "Response Reception"
        RR["Response received:<br/>- Status Code<br/>- Headers<br/>- Body JSON<br/>- Metadata"]
    end
    
    subgraph "Verification"
        V["Verification Functions:<br/>- verify_status_code()<br/>- verify_header()<br/>- verify_json_key()<br/>- verify_json_structure()"]
    end
    
    subgraph "Logging"
        L["Logged to:<br/>- Console<br/>- HTML Report"]
    end
    
    RC --> HR
    HR --> SP
    SP --> RR
    RR --> V
    V --> L
```

---

## Test Payload Generation Flow

```mermaid
graph TD
    Start["Generate Payload<br/>generate_user_payload()"]
    
    A["Step 1: Select Random Name<br/>from names list<br/>10 predefined names"]
    B["Step 2: Generate Random<br/>Number 10-99"]
    C["Step 3: Create Email<br/>Format: name + number<br/>+ @yopmail.com"]
    D["Step 4: Create Payload Dict<br/>{name, email}"]
    E["Return Payload<br/>Ready for API Request"]
    
    Start --> A
    A --> B
    B --> C
    C --> D
    D --> E
    
    style A fill:#fff3e0
    style B fill:#fff3e0
    style C fill:#fff3e0
    style D fill:#fff3e0
    style E fill:#e8f5e9
```

---

## Verification Strategy Flow

```mermaid
graph LR
    subgraph "Response Validation"
        R["API Response<br/>from utils.py"]
    end
    
    subgraph "Verification Steps"
        V1["verify_status_code()<br/>Expected vs Actual"]
        V2["verify_header()<br/>Check Headers Present"]
        V3["verify_json_key()<br/>Check Keys Exist<br/>& Values Match"]
        V4["verify_json_structure()<br/>Validate JSON Type"]
    end
    
    subgraph "Results"
        Pass["PASS<br/>All Verifications<br/>Successful"]
        Fail["FAIL<br/>One or More<br/>Verifications Failed"]
    end
    
    subgraph "Logging"
        Log["Log to Logger<br/>INFO: Success<br/>ERROR: Failure"]
    end
    
    R --> V1
    V1 --> V2
    V2 --> V3
    V3 --> V4
    V4 -->|All Pass| Pass
    V4 -->|Any Fail| Fail
    Pass --> Log
    Fail --> Log
    
    style Pass fill:#c8e6c9
    style Fail fill:#ffcdd2
```

---

## File Import Dependency Graph

```mermaid
graph TB
    Test["test_demo.py"]
    
    Test -->|imports| Const["API_CONSTANT.PY<br/>- URLs<br/>- Headers"]
    Test -->|imports| Payload["payload_manager.py<br/>- Payloads<br/>- generate_user_payload()"]
    Test -->|imports| Utils["utils.py<br/>- get_request()<br/>- post_request()<br/>- put_request()<br/>- delete_request()"]
    
    Utils -->|imports| Requests["requests library<br/>HTTP calls"]
    
    Const -->|defines| URLs["API Endpoints"]
    Payload -->|uses| Random["random library<br/>for unique data"]
    
    Requests --> API["JSONPlaceholder API"]
    
    Test -->|optional| Verify["common_verifications.py<br/>- verify_status_code()<br/>- verify_header()<br/>- verify_json_key()<br/>- verify_json_structure()"]
    
    Verify -->|imports| Logging["logging module"]
    
    Test -->|configured by| Conf["conftest.py<br/>pytest setup"]
    Conf -->|enables| Reports["HTML Report<br/>Generation"]
```

---

## Request Types & Response Expectations

```mermaid
graph TB
    subgraph "GET Requests"
        G1["GET /users"]
        G1_R["Response 200<br/>Returns List"]
        
        G2["GET /users/1"]
        G2_R["Response 200<br/>Returns Object"]
    end
    
    subgraph "POST Requests"
        P1["POST /users<br/>with Payload"]
        P1_R["Response 201<br/>Returns Created<br/>Object with ID"]
    end
    
    subgraph "PUT Requests"
        U1["PUT /users/1<br/>with Payload"]
        U1_R["Response 200<br/>Returns Updated<br/>Object"]
    end
    
    subgraph "DELETE Requests"
        D1["DELETE /users/1"]
        D1_R["Response 200<br/>Confirms Deletion"]
    end
    
    G1 --> G1_R
    G2 --> G2_R
    P1 --> P1_R
    U1 --> U1_R
    D1 --> D1_R
    
    style G1_R fill:#e3f2fd
    style G2_R fill:#e3f2fd
    style P1_R fill:#f3e5f5
    style U1_R fill:#fff3e0
    style D1_R fill:#fce4ec
```

---

## Error Handling & Logging Flow

```mermaid
graph TD
    API["API Request Executed"]
    
    API --> StatusCheck{"Status Code<br/>as Expected?"}
    
    StatusCheck -->|YES| LogPass["Log: SUCCESS<br/>level=INFO"]
    StatusCheck -->|NO| LogFail["Log: FAILURE<br/>level=ERROR"]
    
    LogPass --> JSONCheck{"Valid JSON<br/>Response?"}
    
    LogFail --> Fail1["Test FAILS<br/>Report Generated"]
    
    JSONCheck -->|YES| KeyCheck{"Expected Keys<br/>Present?"}
    JSONCheck -->|NO| JSONErr["Log JSON Error<br/>level=ERROR"]
    
    KeyCheck -->|YES| Pass["Test PASSES<br/>Report Generated"]
    KeyCheck -->|NO| KeyErr["Log Key Missing<br/>level=ERROR"]
    
    JSONErr --> Fail2["Test FAILS<br/>Report Generated"]
    KeyErr --> Fail3["Test FAILS<br/>Report Generated"]
    
    style Pass fill:#c8e6c9
    style Fail1 fill:#ffcdd2
    style Fail2 fill:#ffcdd2
    style Fail3 fill:#ffcdd2
```

---

## Testing Workflow Summary

| Step | Component | Action | Output |
|------|-----------|--------|--------|
| 1 | conftest.py | Initialize pytest & logging | Configured environment |
| 2 | test_demo.py | Load test functions | Test discovery |
| 3 | API_CONSTANT.PY | Load URLs & headers | Configuration data |
| 4 | payload_manager.py | Generate test data | Request payload |
| 5 | utils.py | Make HTTP request | Response object |
| 6 | common_verifications.py | Validate response | Pass/Fail result |
| 7 | conftest.py | Generate report | HTML report file |

---

## Directory & Module Relationship

```mermaid
graph TB
    Root["pytest-crud-framework"]
    
    Root --> Conf["conftest.py<br/>(Global Config)"]
    Root --> Req["requirements.txt"]
    Root --> Doc["README.md<br/>Flow.md"]
    
    Root --> Src["src/"]
    Src --> Config["config/"]
    Src --> Const["constants/<br/>API_CONSTANT.PY"]
    Src --> Help["helpers/<br/>common_verifications.py<br/>payload_manager.py"]
    Src --> Utils["utils/<br/>utils.py"]
    
    Root --> Tests["tests/<br/>test_demo.py"]
    
    Root --> Reports["reports/<br/>(Generated)"]
    
    Conf -.->|used by| Tests
    Const -.->|imported by| Tests
    Help -.->|imported by| Tests
    Utils -.->|imported by| Tests
    
    Tests -.->|generates| Reports
```

---

## Response Verification Chain

```mermaid
flowchart LR
    Resp["Response<br/>Received"]
    
    V1["Step 1:<br/>verify_status_code<br/>Check HTTP Code"]
    V2["Step 2:<br/>verify_header<br/>Check Headers"]
    V3["Step 3:<br/>verify_json_structure<br/>Check JSON Type"]
    V4["Step 4:<br/>verify_json_key<br/>Check Keys/Values"]
    
    V1 -->|Pass| V2
    V2 -->|Pass| V3
    V3 -->|Pass| V4
    V4 -->|Pass| Final["All Verifications<br/>PASSED ✓"]
    
    V1 -->|Fail| FailLog["Log Error &<br/>FAIL Test ✗"]
    V2 -->|Fail| FailLog
    V3 -->|Fail| FailLog
    V4 -->|Fail| FailLog
    
    Resp --> V1
    
    Final --> Pass["Test PASSED<br/>Report Updated"]
    FailLog --> Fail["Test FAILED<br/>Report Updated"]
```

---

## Execution Timeline

```mermaid
timeline
    title Test Execution Timeline
    
    t1 : Start pytest
    t1 : Load conftest.py
    
    t2 : Initialize Logging
    t2 : Setup Report Path
    
    t3 : Discover test_demo.py
    
    t4 : test_get_all_users()
    t4 : GET /users
    t4 : Verify Status 200
    
    t5 : test_get_user_by_id()
    t5 : GET /users/1
    t5 : Verify Status 200
    
    t6 : test_create_user()
    t6 : Generate Payload
    t6 : POST /users
    t6 : Verify Status 201
    
    t7 : put_update_user()
    t7 : PUT /users/1
    t7 : Verify Status 200
    
    t8 : test_delete_user()
    t8 : DELETE /users/1
    t8 : Verify Status 200
    
    t9 : Generate HTML Report
    t9 : Test Execution Complete
```

---

This documentation provides a comprehensive overview of how the pytest-CRUD-Framework operates, from test discovery through report generation.

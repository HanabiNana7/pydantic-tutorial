# Pydantic Tutorial

使用 **Pydantic v2** 示範資料驗證、序列化、設定管理。

---

## 功能說明
| 功能 | 說明 |
| --- | --- |
| **資料模型** | 型別註解 + Runtime 驗證，`model_validate()` / `model_dump()` |
| **自訂驗證** | `field_validator`, `model_validator` 滿足複雜規則 |
| **設定管理** | `BaseSettings` 讀取環境變數、.env 檔 |
| **測試框架** | pytest |

---

## 專案結構

```text
pydantic-tutorial/
├── app/
│   ├── src/pydantic_tutorial/      # 套件原始碼
│   │   ├── models.py               # Pydantic 資料模型
│   │   ├── settings.py             # 設定管理
│   │   └── main.py                 # 範例執行入口
│   └── tests/                      # pytest 測試
```

---

## 使用方法
可直接至 `app\tests\pydantic_tutorial\test_models.py` 參考使用範例

---

## 參考資料
- Pydantic 官方文件：Models、Validators、Settings 等章節

---

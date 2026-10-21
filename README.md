# Playwright Pytest POM Framework - SauceDemo E2E Test Suite

An End-to-End (E2E) Test Automation Framework designed to test the **[SauceDemo](https://www.saucedemo.com/)** web application. This project uses **Python**, **Playwright Sync API**, and **Pytest** structured with the **Page Object Model (POM)** design pattern.

---

## 🛠️ Key Features & Architecture

* **Page Object Model (POM):** UI locators and actions are encapsulated into dedicated page classes (`Loginmainpage`, `Inventorypage`, `Checkoutpage`).
* **Data-Driven Testing (DDT):** Test cases are dynamically parameterized using JSON fixtures (`loginDetails/login_info.json`) via `@pytest.mark.parametrize`
* **Parallel Execution:** Integrated with `pytest-xdist` to run tests across multiple parallel worker threads.
* **Cross-Browser CLI Support:** Custom CLI options (`--browser_name`) configured via `conftest.py` allowing dynamic browser selection (Chrome, Firefox).
* **Rich HTML Reporting:** Automatic standalone HTML test execution reports generated using `pytest-html`.
* **CI/CD Ready:** Automated execution support configured for **Jenkins** builds.

---

## 📁 Repository Structure

```text
├── loginDetails/
│   └── login_info.json          # Test data fixture containing parameterized user credentials
├── pageObjects/
│   ├── login_page.py            # Page Object for SauceDemo Login Page
│   ├── inventory_page.py        # Page Object for Inventory, Product Sorting, & Cart
│   └── checkout_page.py         # Page Object for Checkout Information & Order Confirmation
├── conftest.py                  # Pytest fixtures, browser options, & setup/teardown logic
├── test_e2e_purchase.py         # End-to-End purchase scenario test suite
├── report.html                  # Generated Pytest HTML execution report
└── README.md                    # Project documentation

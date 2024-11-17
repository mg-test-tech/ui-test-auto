# Created by mgelezov at 17/11/2024
Feature: sp_assessment
  SP assessment script with Python and Gherkin

  Scenario Outline: Navigate to Supported Product and assert text
    When user navigates to <URL> user can see navigation bar and item <navbar_item>
    And user clicks on <navbar_item> and clicks on <menu_item> from dropdown menu
    And user redirected to corresponding page <app_page_url>
    And user scrolls down to Additional Features
    And user clicks on Products Supported
    Then user can see the text <product_supported_text>
    Examples:
      | URL                             | navbar_item | menu_item                    | app_page_url                                                  | product_supported_text                         |
      | https://www.matchingengine.com/ | Modules     | Repertoire Management Module | https://www.matchingengine.com/repertoire-management-module/  | There are several types of Product Supported:  |

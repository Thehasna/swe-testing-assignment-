\# Quick-Calc Testing Documentation



This document explains the testing strategy used for the Quick-Calc calculator application. It includes details on unit tests, integration tests, and how these tests relate to software testing concepts discussed in Lecture 3.



\## Testing Strategy



The Quick-Calc application was tested using a combination of unit tests and integration tests. 



\*\*Unit Tests:\*\*  

\- Each core calculator function (add, subtract, multiply, divide, clear) was tested individually.  

\- Edge cases were tested, including division by zero, negative numbers, and decimal numbers.  



\*\*Integration Tests:\*\*  

\- Verified that the calculator interface correctly uses the core functions.  

\- Tested full user flows, such as adding two numbers and then clearing the result.



\## Lecture Concepts

&nbsp;   \*\*Testing Pyramid:\*\*  

\- The Quick-Calc test suite reflects the Testing Pyramid.  

\- Most tests are unit tests (base of the pyramid) for individual functions.  

\- A few integration tests (top of the pyramid) verify that different parts of the application work together.



&nbsp;   \*\*Black-box vs White-box Testing:\*\*  

\- Unit tests use \*\*white-box testing\*\*, because we know how each function works internally.  

\- Integration tests use \*\*black-box testing\*\*, focusing on inputs and outputs without considering the internal code.



&nbsp;    \*\*Regression Testing:\*\*  

\- The test suite can be re-run whenever changes are made to catch regressions.  

\- For example, if a future update changes the divide function, running all tests will detect any broken functionality.



\## Test Results Summary 



&nbsp;  | Test Name                   | Type         | Status |

|------------------------------|-------------|--------|

| test\_addition                | Unit        | Pass   |

| test\_subtraction             | Unit        | Pass   |

| test\_multiplication          | Unit        | Pass   |

| test\_division                | Unit        | Pass   |

| test\_division\_by\_zero        | Unit        | Pass   |

| test\_negative\_numbers        | Unit        | Pass   |

| test\_decimal\_numbers         | Unit        | Pass   |

| test\_clear                   | Unit        | Pass   |

| test\_full\_addition\_flow      | Integration | Pass   |

| test\_clear\_after\_calculation | Integration | Pass   |


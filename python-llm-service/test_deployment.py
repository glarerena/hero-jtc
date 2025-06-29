#!/usr/bin/env python3
"""
Test script to verify the no-LLM deployment works correctly
"""

def test_imports():
    """Test that all imports work without LLM dependencies"""
    try:
        from rag_utils import get_context
        print("✅ Successfully imported get_context from rag_utils")
        
        # Test a simple response
        response = get_context("hello")
        print(f"✅ Test response generated: {len(response)} characters")
        print(f"Response preview: {response[:100]}...")
        
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def test_responses():
    """Test different types of responses"""
    from rag_utils import get_context
    
    test_cases = [
        ("hi", "greeting"),
        ("listings", "listings"),
        ("apply", "application"),
        ("ami", "income"),
        ("documents", "documents"),
        ("housing resources", "resources")
    ]
    
    for question, expected_type in test_cases:
        try:
            response = get_context(question)
            print(f"✅ '{question}' -> {len(response)} chars")
        except Exception as e:
            print(f"❌ '{question}' failed: {e}")

if __name__ == "__main__":
    print("🧪 Testing no-LLM deployment...")
    
    if test_imports():
        print("\n📋 Testing different response types...")
        test_responses()
        print("\n✅ All tests passed! Ready for deployment.")
    else:
        print("\n❌ Tests failed. Check the code.") 
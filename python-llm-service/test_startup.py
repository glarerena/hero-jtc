#!/usr/bin/env python3
"""
Simple test to verify the app can start correctly
"""

def test_imports():
    """Test that all imports work"""
    try:
        from app import app
        print("✅ Successfully imported FastAPI app")
        
        from rag_utils import get_context
        print("✅ Successfully imported get_context")
        
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality"""
    try:
        from rag_utils import get_context
        
        # Test a simple response
        response = get_context("hello")
        print(f"✅ Test response: {len(response)} characters")
        
        return True
    except Exception as e:
        print(f"❌ Functionality test failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing app startup...")
    
    if test_imports() and test_basic_functionality():
        print("✅ All tests passed! App is ready for deployment.")
    else:
        print("❌ Tests failed.") 
# Ruby Solutions - Parallel Implementation

**Why Ruby + Rust?**

- **Rust**: Systems-level understanding, performance, ownership/borrowing
- **Ruby**: High-level expressiveness, rapid prototyping, clarity

**Learning benefit**: Implementing in both languages deepens understanding of the algorithm itself, not just language syntax.

---

## 📁 Structure

```
src_ruby/
├── README.md                    ← You are here
├── patterns/
│   ├── two_pointers/
│   │   ├── problem_001_two_sum_ii.rb
│   │   ├── problem_001_two_sum_ii_spec.rb
│   │   └── ...
│   ├── sliding_window/
│   └── ...
├── lib/
│   ├── tracer.rb                ← Execution tracing for visualization
│   └── test_helper.rb           ← Test utilities
└── Gemfile                      ← Ruby dependencies
```

---

## 🚀 Setup

### Install Ruby (if not done)

```bash
sudo apt-get install -y ruby-full
ruby --version
```

### Install Dependencies

```bash
cd ~/dsa-mastery/src_ruby
bundle install
```

---

## 📝 Your Workflow

### For Each Problem:

1. **Solve in Rust first** (primary)
   - `src/patterns/two_pointers/problem_001.rs`
   - Get PR reviewed
   - Merge

2. **Optional: Solve in Ruby** (reinforcement)
   - `src_ruby/patterns/two_pointers/problem_001.rb`
   - Implement same algorithm
   - Compare approach
   - Generate visualization from Ruby too

3. **Compare both** - Deepen understanding

---

## 🧪 Testing

### Run Tests

```bash
# Single file
ruby src_ruby/patterns/two_pointers/problem_001_two_sum_ii_spec.rb

# All tests in pattern
ruby -Ilib -e 'Dir.glob("src_ruby/patterns/two_pointers/*_spec.rb").each { |f| require_relative f }'

# With RSpec (if installed)
rspec src_ruby/patterns/two_pointers/
```

---

## 🎬 Visualization from Ruby

```bash
# Run with tracing
ruby src_ruby/patterns/two_pointers/problem_001_two_sum_ii.rb \
  --trace \
  --input "[2,7,11,15]" \
  --target 9 \
  > trace_data.json

# Generate video (same as Rust)
manim scripts/visualize/callstack_viz.py TwoPointersScene -pql
```

---

## 📊 Template Structure

### Ruby Solution Template

```ruby
# src_ruby/patterns/two_pointers/problem_001_two_sum_ii.rb

require_relative '../../lib/tracer'

class Solution
  include Tracer

  # LeetCode #167: Two Sum II - Input Array Is Sorted
  #
  # @param {Integer[]} numbers - Sorted array of integers
  # @param {Integer} target - Target sum
  # @return {Integer[]} - 1-indexed positions
  #
  # Approach:
  #   TODO: Explain approach
  #
  # Complexity:
  #   Time: O(?) - TODO
  #   Space: O(?) - TODO
  #
  def two_sum(numbers, target)
    left = 0
    right = numbers.length - 1

    trace(:init, {left: left, right: right})

    while left < right
      sum = numbers[left] + numbers[right]

      trace(:iteration, {
        left: left,
        right: right,
        sum: sum
      })

      return [left + 1, right + 1] if sum == target

      if sum < target
        left += 1
      else
        right -= 1
      end
    end

    # Should never reach here per problem constraints
    []
  end
end

# Tests
if __FILE__ == $0
  require 'test/unit'

  class TwoSumIITest < Test::Unit::TestCase
    def setup
      @solution = Solution.new
    end

    def test_example_1
      assert_equal([1, 2], @solution.two_sum([2, 7, 11, 15], 9))
    end

    def test_example_2
      assert_equal([1, 3], @solution.two_sum([2, 3, 4], 6))
    end

    def test_example_3
      assert_equal([1, 2], @solution.two_sum([-1, 0], -1))
    end

    def test_two_elements
      assert_equal([1, 2], @solution.two_sum([1, 2], 3))
    end

    def test_negatives
      assert_equal([2, 4], @solution.two_sum([-10, -5, 0, 5, 10], 0))
    end
  end
end
```

---

## 🔄 Rust vs Ruby Comparison

### Two Pointers - Two Sum II

**Rust:**
```rust
pub fn two_sum(numbers: &[i32], target: i32) -> Vec<i32> {
    let mut left = 0;
    let mut right = numbers.len() - 1;

    while left < right {
        let sum = numbers[left] + numbers[right];

        match sum.cmp(&target) {
            Ordering::Equal => return vec![(left + 1) as i32, (right + 1) as i32],
            Ordering::Less => left += 1,
            Ordering::Greater => right -= 1,
        }
    }

    vec![]
}
```

**Ruby:**
```ruby
def two_sum(numbers, target)
  left = 0
  right = numbers.length - 1

  while left < right
    sum = numbers[left] + numbers[right]

    return [left + 1, right + 1] if sum == target

    sum < target ? left += 1 : right -= 1
  end

  []
end
```

**Key Differences:**
- Rust: Explicit types, borrowing (`&[i32]`), match expressions
- Ruby: Duck typing, implicit returns, ternary operators
- **Same algorithm, different expression**

---

## 💡 When to Use Ruby

### Good for Ruby:
- ✅ **Rapid prototyping** - Test algorithm logic quickly
- ✅ **String manipulation** - Ruby excels here
- ✅ **Quick iteration** - Faster development cycle
- ✅ **Teaching** - More readable for explaining concepts

### Stick with Rust:
- ✅ **Performance critical** - Rust is orders of magnitude faster
- ✅ **Memory constraints** - Rust gives fine control
- ✅ **Concurrency** - Rust's safety guarantees
- ✅ **Interview primary** - Most top companies prefer systems languages

### Recommended Approach:
1. **Always solve in Rust first** (primary submission)
2. **Optionally solve in Ruby** to reinforce understanding
3. **Compare implementations** - see algorithm more clearly
4. **Use Ruby for rapid experimentation** when stuck

---

## 🎯 Senior-Level Insight

**Google interviewer**: "Can you implement this in another language?"

**You**: "Absolutely. Here's the Ruby version..."

*Writes clean Ruby implementation in 2 minutes*

**Interviewer**: Impressed - You understand the algorithm, not just syntax.

---

## 📚 Resources

- **Ruby Style Guide**: https://rubystyle.guide/
- **RSpec Testing**: https://rspec.info/
- **Ruby Performance**: https://github.com/JuanitoFatas/fast-ruby

---

**Ruby is optional but powerful for deepening understanding.**

**Your call whether to implement both or just Rust.** 🔴

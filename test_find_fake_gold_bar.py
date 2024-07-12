from seleniumbase import BaseCase

class TestCase(BaseCase):

    # Function to fill left bowl with entered list
    def fill_left_bowl(self, bar_list=[]):
        for i in range(len(bar_list)):
            self.type(
                f'input[data-side="left"][data-index="{i}"]', bar_list[i]
            )

    # Function to fill right bowl with entered list
    def fill_right_bowl(self, bar_list=[]):
        for i in range(len(bar_list)):
            self.type(
                f'input[data-side="right"][data-index="{i}"]', bar_list[i]
            )

    # Function to split the lighter bowl in half to the left and right bowls
    def split_weights(self, result="", left_bowl=[], right_bowl=[]):
        print(f'Old Left Bowl: {left_bowl}')
        print(f'Old Right Bowl: {right_bowl}')
        if "<" == result:
            print('New Left Bowl: '+ str(left_bowl[:len(left_bowl)//2]))
            print('New Right Bowl: '+ str(left_bowl[len(left_bowl)//2:]))
            return left_bowl[:len(left_bowl)//2], left_bowl[len(left_bowl)//2:]

        elif ">" == result:
            print('New Left Bowl: ' + str(right_bowl[:len(right_bowl)//2]))
            print('New Right Bowl: ' + str(right_bowl[len(right_bowl)//2:]))
            return right_bowl[:len(right_bowl)//2], right_bowl[len(right_bowl)//2:]
        else:
            raise Exception("Invalid Result!")

    def test_find_fake_gold_bar(self):
        answer = ""
        left_bowl = ['0','1','2','3']
        right_bowl = ['4','5','6','7']

        # Open exercise page
        self.open('http://sdetchallenge.fetch.com')
        self.wait_for_element('.game')

        # Initialize setup (split left bowl and right bowl with 4 numbers each)
        # Left bowl: [0, 1, 2, 3]
        self.fill_left_bowl(left_bowl)
        # Right bowl: [4, 5, 6, 7]
        self.fill_right_bowl(right_bowl)

        # Click the Weight button and assess results
        self.click('button#weigh')
        self.wait_for_text_not_visible('?', '.result button#reset')
        result = self.get_text('.result button#reset')
        self.assert_false("?" in result)  # Asserts Result has changed
        print(f'\nResult: {result}\n')
        self.save_screenshot_to_logs(name='First Weighting Result')

        # If the bowls are equal, the fake bar is "8"
        if "=" == result:
            answer = "8"
            print(f'Answer is Gold Bar Number {answer}')
            self.jquery_click('button#coin_8')
            self.switch_to_alert()
            self.assert_true("Yay! You find it!" == self.accept_alert())
            self.save_screenshot_to_logs(name='Weighting Result')
            return
        
        # Otherwise, split the lighter bowl into the two bowls
        left_bowl, right_bowl = self.split_weights(result, left_bowl, right_bowl)

        # Clear gameboard
        self.click('button#reset:not([disabled]')
        self.wait_for_text('?', '.result button#reset')

        # Refill bowls with remaining bars from the lighter bowl
        self.fill_left_bowl(left_bowl)
        self.fill_right_bowl(right_bowl)

        # Repeat previous steps to check results and resplit the bowls
        self.click('button#weigh')
        self.wait_for_text_not_visible('?', '.result button#reset')
        result = self.get_text('.result button#reset')
        self.save_screenshot_to_logs(name='Second Weighting Result')
        left_bowl, right_bowl = self.split_weights(result, left_bowl, right_bowl)
        self.click('button#reset:not([disabled]')
        self.wait_for_text('?', '.result button#reset')
        self.fill_left_bowl(left_bowl)
        self.fill_right_bowl(right_bowl)

        # Down to 2 last bars, the lighter bowl is the answer
        self.click('button#weigh')
        self.wait_for_text_not_visible('?', '.result button#reset')
        result = self.get_text('.result button#reset')
        if "<" in result:
            answer = ''.join(left_bowl)
        elif ">" in result:
            answer = ''.join(right_bowl)
        print(f'Answer is Gold Bar Number {answer}')
        self.jquery_click(f'.coins > button#coin_{answer}')
        self.switch_to_alert()
        self.assert_true("Yay! You find it!" == self.accept_alert())
        self.save_screenshot_to_logs(name='Final Weighting Result')

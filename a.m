chipher_text = "";
key = 3;
plain_text = upper(input("Enter plain text: ", 's'));
for i = 1:length(plain_text)
    chr = plain_text(i);
    if isstrprop(chr, 'alpha')
        shifted_value = mod(double(chr)-double('A') +key, 26);
        cipher_char = char(shifted_value+double('A')); 
        chipher_text = chipher_text + cipher_char;
    else
        chipher_text = chipher_text + chr; 
    end
end

fprintf("Ciphered Text: %s\n", chipher_text);
plain_text = "";
key = 3;
cipher_text = upper(input("Enter cipher: ", 's'));
for i = 1:length(cipher_text)
    chr = cipher_text(i);
    if isstrprop(chr, 'alpha')
        shifted_value = mod(double(chr) - double('A') - key, 26);
        plain_char = char(shifted_value + double('A'));
        plain_text = plain_text + plain_char;
    else
        plain_text = plain_text + chr;
    end
end

fprintf("Plain Text: %s\n", plain_text);

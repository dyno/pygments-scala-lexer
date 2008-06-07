class ScalaLexer(RegexLexer):
    name = 'Scala'
    aliases = ['scala']
    filenames = '*.scala'
    flags = re.MULTILINE | re.DOTALL

    #: optional Comment or Whitespace
    _ws = r'(?:\s|//.*?\n|/[*].*?[*]/)+'

    tokens = {
       'root': [
           # method names
           (r'^(\s*(?:[a-zA-Z_][a-zA-Z0-9_\.\[\]]*\s+)+?)' # return arguments
            r'([a-zA-Z_][a-zA-Z0-9_]*)'                    # method name
            r'(\s*)(\()',                                  # signature start
            bygroups(using(this), Name.Function, Text, Operator)),
           (r'[^\S\n]+', Text),
           (r'//.*?\n', Comment),
           (r'/\*.*?\*/', Comment),
           (r'@[a-zA-Z_][a-zA-Z0-9_\.]*', Name.Decorator),
           (r'(abstract|case|catch|class|do|else|extends|false|final|'
            r'finally|for|forSome|if|implicit|import|lazy|match|new|null|'
            r'object|override|package|private|protected|requires|return|'
            r'sealed|super|this|throw|trait|try|true|type|while|with|yield|'
            r'_|:|=|=>|<-|<:|<%|>:|#|@)\b', Keyword),
           (r'(if|else|(else\s*if)|match|case)', Keyword),
           (r'(def|var|val)', Keyword.Declaration),
           (r'(String|Char|Int|Float|Double|Boolean)', Keyword.Type),
           (r'(boolean|byte|char|double|float|int|long|short|void)\b',
            Keyword.Type),
           (r'(true|false|null|\(\))\b', Keyword.Constant),
           (r'(class|object|trait)(\s+)', bygroups(Keyword, Text), 'class'),
           (r'(import)(\s+)', bygroups(Keyword, Text), 'import'),
           (r'"(\\\\|\\"|[^"])*"', String),
           (r"'\\.'|'[^\\]'|'\\u[0-9a-f]{4}'", String.Char),
           (r'(\.)([a-zA-Z_][a-zA-Z0-9_]*)', bygroups(Operator, Name.Attribute)),
           (r'[a-zA-Z_][a-zA-Z0-9_]*:', Name.Label),
           (r'[a-zA-Z_\$][a-zA-Z0-9_]*', Name),
           #(r'[~\^\*!%&\[\]\(\)\{\}<>\|+=:;,./?-]', Operator),
           (r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
           (r'0x[0-9a-f]+', Number.Hex),
           (r'[0-9]+', Number.Integer),
           (r'\n', Text)
       ],
       'class': [
           (r'[a-zA-Z_][a-zA-Z0-9_]*', Name.Class, '#pop')
       ],
       'import': [
           (r'[a-zA-Z0-9_.]+\*?', Name.Namespace, '#pop')
       ],
   }

